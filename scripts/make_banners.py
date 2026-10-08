"""Draw the profile README's section banners into assets/banners.

Usage: python3 scripts/make_banners.py

Each banner is a 1600 by 120 PNG: a horizontal gradient bar with
rounded corners, the title in white centered over a short gold line,
transparent outside the corners. The gradient runs from #12357a to
#2456b8, which stays distinct from GitHub's dark, dimmed, and light
page backgrounds, so one file serves every theme. The title is set
large enough to read when a phone shows the banner at about a fifth of
its size. Drawn at four times the size and scaled down so the text and
corners are smooth. The font is Lato Black, read from the system font
directory; Lato is under the SIL Open Font License.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BANNERS = {
    "start-here": "Start Here",
    "design-and-architecture": "Design and Architecture",
    "references-and-study-tools": "References and Study Tools",
    "certifications": "Certifications",
    "skills-and-tools": "Skills and Tools",
    "areas-of-focus": "Areas of Focus",
}
OUT = Path(__file__).resolve().parent.parent / "assets" / "banners"

WIDTH, HEIGHT = 1600, 120
LEFT, RIGHT = (0x12, 0x35, 0x7A), (0x24, 0x56, 0xB8)
GOLD = (0xF4, 0xB8, 0x1C)
WHITE = (255, 255, 255)
FONT = "/usr/share/fonts/truetype/lato/Lato-Black.ttf"
FONT_SIZE = 64
RADIUS = 10
LINE_WIDTH, LINE_HEIGHT, LINE_GAP = 160, 5, 12
SCALE = 4


def banner(title: str) -> Image.Image:
    w, h, s = WIDTH * SCALE, HEIGHT * SCALE, SCALE

    gradient = Image.new("RGB", (w, 1))
    for x in range(w):
        t = x / (w - 1)
        gradient.putpixel((x, 0), tuple(round(a + (b - a) * t) for a, b in zip(LEFT, RIGHT)))
    bar = gradient.resize((w, h))

    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), radius=RADIUS * s, fill=255)
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    img.paste(bar, (0, 0), mask)

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, FONT_SIZE * s)
    # Center the title's cap height, the gap, and the line as one block,
    # so every banner places its title and line identically.
    cap_top, cap_bottom = font.getbbox("H")[1], font.getbbox("H")[3]
    cap = cap_bottom - cap_top
    block = cap + LINE_GAP * s + LINE_HEIGHT * s
    top = (h - block) / 2
    text_w = draw.textlength(title, font=font)
    draw.text(((w - text_w) / 2, top - cap_top), title, font=font, fill=WHITE)

    line_top = top + cap + LINE_GAP * s
    lx = (w - LINE_WIDTH * s) / 2
    draw.rounded_rectangle((lx, line_top, lx + LINE_WIDTH * s, line_top + LINE_HEIGHT * s),
                           radius=LINE_HEIGHT * s / 2, fill=GOLD)
    return img.resize((WIDTH, HEIGHT), Image.LANCZOS)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, title in BANNERS.items():
        banner(title).save(OUT / f"{name}.png", optimize=True)
        print(f"{name}.png  {title}")
