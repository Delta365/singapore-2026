"""Write the public copy of the trip map: flight details removed, noindex added.

Usage: python3 -I publish/redact.py SOURCE.html DEST.html

Exits non-zero, without writing DEST, if any flight detail survives.
"""
import os
import re
import sys

# Carriers that fly India to Singapore: Singapore Airlines, Scoot, Air India, IndiGo.
FLIGHT_NO = r"\b(?:SQ|TR|AI|6E)\s?\d{2,4}\b"

# The booked flight times and the check-in cut-off, one per line, live in a
# git-ignored file so they never reach the public repo.
TIMES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flight_times.local")


def load_flight_times():
    try:
        with open(TIMES_FILE, encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        sys.exit(f"Missing {TIMES_FILE}: list the flight times there, one per line.")


FLIGHT_TIMES = load_flight_times()

# Any sentence holding a flight number or one of the flight times is dropped.
FLIGHT_DETAIL = (
    r"(?:" + FLIGHT_NO + "|" + "|".join(r"\b" + re.escape(t) + r"\b" for t in FLIGHT_TIMES) + ")"
)

NOINDEX = '<meta name="robots" content="noindex, nofollow">'

# The "Flights" line in the page header.
FLIGHTS_FACT = re.compile(r'\s*<div class="fact"><b>Flights?</b>.*?</div>', re.S)

# A sentence with a flight detail, followed by another sentence in the
# same string or element. The leading whitespace is kept for the next sentence.
SENTENCE_MID = re.compile(
    r'(?<=[".>])(\s*)[^".<>]*?' + FLIGHT_DETAIL + r'[^"<>]*?\.\s+(?=[^\s"<])'
)
# A sentence with a flight detail that ends its string or element.
SENTENCE_END = re.compile(r'(?<=[".>])\s*[^".<>]*?' + FLIGHT_DETAIL + r'[^"<>]*?(?=["<])')


def redact(html):
    html = FLIGHTS_FACT.sub("", html)
    html = SENTENCE_MID.sub(r"\1", html)
    html = SENTENCE_END.sub("", html)
    if NOINDEX not in html:
        html = re.sub(r"(<head(?:\s[^>]*)?>)", r"\1\n" + NOINDEX, html, count=1)
    return html


def leftovers(html):
    checks = [FLIGHT_NO, r">\s*Flights?\s*<", r"\bSIA\b"]
    checks += [r"\b" + re.escape(t) + r"\b" for t in FLIGHT_TIMES]
    found = []
    for pattern in checks:
        for m in re.finditer(pattern, html):
            found.append(html[max(0, m.start() - 70) : m.end() + 70].replace("\n", " "))
    return found


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__.strip())
    src, dest = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        original = f.read()
    public = redact(original)

    problems = leftovers(public)
    if problems:
        print("Flight details remain; nothing written. Context:", file=sys.stderr)
        for p in problems:
            print("  ..." + p + "...", file=sys.stderr)
        sys.exit(1)
    # A pattern that matched far too much would show up as a large size drop.
    if len(public) < 0.95 * len(original):
        sys.exit(f"Public copy is {len(original) - len(public)} bytes shorter than the source; nothing written.")

    with open(dest, "w", encoding="utf-8") as f:
        f.write(public)
    print(f"    wrote {dest} ({len(original) - len(public)} bytes removed)")


if __name__ == "__main__":
    main()
