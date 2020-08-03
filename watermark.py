#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
----------------------------------------------------------------------------------------------------
* Project Name : AddWatermark
* File Name    : watermark.py
* Description  : Add watermark for images
* Create Time  : 2020-08-03 18:27:29
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh/AddWatermark
----------------------------------------------------------------------------------------------------
* Notice
-
-
----------------------------------------------------------------------------------------------------
'''

try:
    from PIL import Image, ImageDraw, ImageFont
except ModuleNotFoundError:
    print('Module not found.')
    print('Try `pip install -r requirements.txt`')


def add_text_to_image(image, text):
    font = ImageFont.truetype('./fonts/FZXIANGSU24.ttf', 36)

    # 添加背景
    new_img = Image.new('RGBA', (image.size[0] * 3, image.size[1] * 3), (0, 0, 0, 0))
    new_img.paste(image, image.size)

    # 添加水印
    font_len = len(text)
    rgba_image = new_img.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    for i in range(0, rgba_image.size[0], font_len*40+100):
        for j in range(0, rgba_image.size[1], 200):
            image_draw.text((i, j), text, font=font, fill=(0, 0, 0, 50))
    text_overlay = text_overlay.rotate(-45)
    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    # 裁切图片
    image_with_text = image_with_text.crop((image.size[0], image.size[1], image.size[0] * 2, image.size[1] * 2))
    return image_with_text


if __name__ == '__main__':
    input_name = input('输入图片名称(含后缀):\n>>> ')
    output_name = input('输出文件名称(不含后缀):\n>>> ')

    img = Image.open(input_name)
    im_after = add_text_to_image(img, '本文件仅用于' + input('本文件用途:\n>>> '))

    # 保存后的图片文件，后缀必须为.png
    im_after.save(output_name + '.png')

    imgnew = im_after.convert('RGB')
    imgnew.save(output_name + '.pdf')   # 后缀非.png ，可为.jpg等等
