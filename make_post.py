from datetime import datetime
import os
import argparse
from PIL import Image, ImageDraw, ImageFont
import textwrap

# SETTINGS
IMG_SIZE = (1080, 1080)  # Square
BG_COLOR = (255, 255, 255)  # White background
TEXT_COLOR = (0, 0, 0)  # Black text

# FONT_PATH = "/System/Library/Fonts/Supplemental/Courier New.ttf"
FONT_PATH = "Courier New.ttf"  # Change to a font you have
FONT_SIZE = 60
LINE_SPACING = 10  # Pixels between lines

PAPER_TEXTURES = {
    "lined": "paper_textures/lined_paper.jpg",
    "plain": "paper_textures/plain_paper.jpg",
    "sticky": "paper_textures/sticky_note.jpg",
    "paper": None
}

def get_configs():
    pass
    # parser = argparse.ArgumentParser(description="Make a new post (if it has spaces, make sure to use double quotes!!)")
    # parser.add_argument('--cat', type=str, help="What're you writing about?")
    # parser.add_argument('--title', type=str, help="What's the name of the thing you are writing?")
    # args = parser.parse_args()
    # return args 

def create_instagram_image(text, output_path, template_name = 'paper'):
    # from template
    if template_name not in PAPER_TEXTURES:
        raise ValueError(f"Template '{template_name}' not found.")
    
    # Load paper background
    # bg = Image.open(PAPER_TEXTURES[template_name]).convert("RGB")
    bg = bg.resize(IMG_SIZE)
    # draw = ImageDraw.Draw(bg)

    # # Create blank image
    img = Image.new("RGB", IMG_SIZE, BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Load font
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # Wrap text to fit image width
    max_width = IMG_SIZE[0] - 100
    lines = []
    for line in text.split("\n"):
        lines.extend(textwrap.wrap(line, width=40))  # Adjust width as needed

    # Measure text block size
    line_heights = [draw.textbbox((0, 0), l, font=font)[3] for l in lines]
    total_height = sum(line_heights) + LINE_SPACING * (len(lines) - 1)
    y_start = (IMG_SIZE[1] - total_height) / 2

    # Draw each line centered
    y = y_start
    for line in lines:
        w = draw.textbbox((0, 0), line, font=font)[2]
        x = (IMG_SIZE[0] - w) / 2
        draw.text((x, y), line, fill=TEXT_COLOR, font=font)
        y += draw.textbbox((0, 0), line, font=font)[3] + LINE_SPACING

    # Save image
    img.save(output_path)
    print(f"Saved {output_path}")

def create_carousel(pages, base_filename):
    os.makedirs("output", exist_ok=True)
    for i, text in enumerate(pages, start=1):
        output_path = f"output/{base_filename}_page{i}.png"
        create_instagram_image(text, output_path)

if __name__ == "__main__":
    # EXAMPLE USAGE
    pages_text = [
        """Page 1: Hello Instagram!
        and there's new lines allowed as well... but it will automatcially make a new line so idk if you need one but you might
        """,
        "Page 2: This is a carousel.",
        "Page 3: Generated automatically with Python."
    ]
    create_carousel(pages_text, "my_post")