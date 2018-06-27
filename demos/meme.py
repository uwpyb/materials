from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import sys
import os


def make_meme(top_text: str, bottom_text: str, filename: str):
    proj_path = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(proj_path, "files")

    font_path = os.path.join(img_path, "Impact.ttf")
    print(filename)
    img = Image.open(os.path.join(img_path, filename))
    image_size = img.size

    # find biggest font size that works
    font_size = int(image_size[1] / 5)
    font = ImageFont.truetype(font_path, font_size)
    top_text_size = font.getsize(top_text)
    bottom_text_size = font.getsize(bottom_text)
    while top_text_size[0] > image_size[0] - 20 or bottom_text_size[0] > image_size[0] - 20:
        font_size = font_size - 1
        font = ImageFont.truetype(font_path, font_size)
        top_text_size = font.getsize(top_text)
        bottom_text_size = font.getsize(bottom_text)

    # find top centered position for top text
    top_text_position_x = (image_size[0] / 2) - (top_text_size[0] / 2)
    top_text_position_y = 0
    top_text_position = (top_text_position_x, top_text_position_y)

    # find bottom centered position for bottom text
    bottom_text_position_x = (image_size[0] / 2) - (bottom_text_size[0] / 2)
    bottom_text_position_y = image_size[1] - bottom_text_size[1]
    bottom_text_position = (bottom_text_position_x, bottom_text_position_y)

    draw = ImageDraw.Draw(img)

    # draw outlines
    # there may be a better way
    outline_range = int(font_size / 15)
    for x in range(-outline_range, outline_range + 1):
        for y in range(-outline_range, outline_range + 1):
            draw.text((top_text_position[0] + x, top_text_position[1] + y), top_text, (0, 0, 0), font=font)
            draw.text((bottom_text_position[0] + x, bottom_text_position[1] + y), bottom_text, (0, 0, 0), font=font)

    draw.text(top_text_position, top_text, (255, 255, 255), font=font)
    draw.text(bottom_text_position, bottom_text, (255, 255, 255), font=font)

    img.save("%s/temp.png" % img_path)


if __name__ == '__main__':
    # TODO: add some proper argument parsing

    top_str = "Not sure if useful"
    bottom_str = "Or wasteful"
    file_nm = "not_sure_if.jpg"
    make_meme(top_str, bottom_str, file_nm)
