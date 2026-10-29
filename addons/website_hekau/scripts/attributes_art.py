"""Ring diagram art of the Hekau Attributes block for any number of list items.

The Figma art (static/src/img/svc/attributes_art.svg, "Frame 7829") connects the
hub to seven 44px pills, 80px apart, with dashed lines: one straight to the middle
pill, three branching up and three down from a trunk at x=481, each turning right
with a 40.5px curve and ending at the pills (x=583). This script redraws the
connectors for another count, centred on the hub, and keeps the rest of the art:

    python3 scripts/attributes_art.py 6   ->  static/src/img/svc/attributes_art_6.svg
"""
import re
import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
SRC = MODULE / 'static/src/img/svc/attributes_art.svg'

HUB_X, HUB_Y = 223, 262      # where the hub line starts (Figma: 223, 264 / branches from 261)
TRUNK_X, PILL_X = 481, 583
PITCH = 80                   # 44px pill + 36px gap
RADIUS = 40.5
LIGHT, DARK = '#8481F2', '#4C4B8C'  # Figma connector gradient (trunk -> pill)


def centres(n):
    """Pill centres, symmetric about the hub line."""
    first = HUB_Y - (n - 1) * PITCH / 2
    return [first + i * PITCH for i in range(n)]


def connector(y):
    if abs(y - HUB_Y) < 1:
        return f'M{TRUNK_X} {HUB_Y}H{PILL_X}'
    sign = -1 if y < HUB_Y else 1
    corner = y - sign * RADIUS
    sweep = 1 if sign < 0 else 0
    return (f'M{TRUNK_X} {HUB_Y}V{corner:g}'
            f'A{RADIUS} {RADIUS} 0 0 {sweep} {TRUNK_X + RADIUS:g} {y:g}H{PILL_X}')


def build(n):
    svg = SRC.read_text()
    # Drop Figma's seven connectors ("Vector 5" to "Vector 11"), keep the hub.
    for name in ('Vector 5', 'Vector 6', 'Vector 7', 'Vector 8', 'Vector 9', 'Vector 10', 'Vector 11'):
        start = svg.index(f'<g data-n="{name}"')
        depth, pos = 0, start
        for m in re.finditer(r'<g\b|</g>', svg[start:]):
            depth += 1 if m.group() != '</g>' else -1
            if depth == 0:
                pos = start + m.end()
                break
        svg = svg[:start] + svg[pos:]
    paths = [f'M{HUB_X} {HUB_Y}H{TRUNK_X}'] + [connector(y) for y in centres(n)]
    lines = (f'<g data-n="Connectors" fill="none" stroke="url(#hk-conn)" stroke-width="1" '
             f'stroke-dasharray="6 6" stroke-dashoffset="3">'
             + ''.join(f'<path d="{d}"/>' for d in paths) + '</g>')
    grad = (f'<linearGradient id="hk-conn" gradientUnits="userSpaceOnUse" x1="{TRUNK_X}" y1="0" x2="{PILL_X}" y2="0">'
            f'<stop offset="0" stop-color="{LIGHT}"/><stop offset="1" stop-color="{DARK}"/></linearGradient>')
    svg = svg.replace('<defs>', '<defs>' + grad, 1)
    # Connectors under the hub (as in Figma: the line starts inside the rings).
    first_group = svg.index('<g', svg.index('</defs>'))
    inner = svg.index('>', first_group) + 1
    svg = svg[:inner] + lines + svg[inner:]
    return svg


if __name__ == '__main__':
    count = int(sys.argv[1])
    out = MODULE / f'static/src/img/svc/attributes_art_{count}.svg'
    out.write_text(build(count))
    print('wrote', out.relative_to(MODULE), centres(count))
