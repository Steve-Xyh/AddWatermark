#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
----------------------------------------------------------------------------------------------------
* Project Name : AddWatermark
* File Name    : pdf_watermark.py
* Description  : Add watermarks for each page in pdf files.
* Create Time  : 2020-08-03 17:12:25
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh/AddWatermark
----------------------------------------------------------------------------------------------------
* Notice
- Have problems with `GBK` encoded PDF.(caused by PyPDF2 library)
----------------------------------------------------------------------------------------------------
'''


# XXX(Steve X): Have problems with `GBK` encoded PDF.(caused by PyPDF2 library)


try:
    import os
    from PyPDF2 import PdfFileWriter, PdfFileReader
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import cm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
except ModuleNotFoundError:
    print('Module not found.')
    print('Try `pip install -r requirements.txt`')


# 文件保存目录
BASE_DIR = './'

# 添加中文字体
font_dir = os.path.join(BASE_DIR, "./fonts/FZXIANGSU24.ttf")
pdfmetrics.registerFont(TTFont('font', font_dir))


def create_watermark(content) -> PdfFileReader:
    """创建PDF水印模板"""

    watermark_pdf = os.path.join(BASE_DIR, 'watermark.pdf')

    # 使用reportlab来创建一个PDF文件来作为一个水印文件
    wm_canvas = canvas.Canvas(watermark_pdf)
    wm_canvas.translate(10*cm, 5*cm)
    wm_canvas.setFont('font', 30)

    # 设置水印文件
    wm_canvas.saveState()

    # 设置不透明度
    wm_canvas.setFillAlpha(0.2)
    wm_canvas.rotate(45)

    content += ' '*3
    x_step = len(content)
    y_step = 5
    for x in range(-10, 10):
        for y in range(-10, 10):
            wm_canvas.drawString(x * cm * x_step, y * cm * y_step, content)

    wm_canvas.restoreState()
    wm_canvas.save()
    pdf_watermark = PdfFileReader(open(watermark_pdf, "rb"), strict=False)

    return pdf_watermark


def add_watermark(input_file, watermark_file: PdfFileReader, output_file):
    pdf_output = PdfFileWriter()
    input_stream = open(input_file, 'rb')
    pdf_input = PdfFileReader(input_stream, strict=False)

    page_num = pdf_input.getNumPages()

    # 给每一页打水印
    for i in range(page_num):
        page = pdf_input.getPage(i)
        page.mergePage(watermark_file.getPage(0))
        page.compressContentStreams()  # 压缩内容
        pdf_output.addPage(page)
    pdf_output.write(open(output_file, 'wb'))


if __name__ == "__main__":
    input_name = input('输入文件名称(含后缀):\n>>> ')
    output_name = input('输出文件名称(含后缀):\n>>> ')

    pdf_file_mark = create_watermark('本文件仅用于' + input('本文件用途:\n>>> '))
    pdf_file_in = os.path.join(BASE_DIR, input_name)
    pdf_file_out = os.path.join(BASE_DIR, output_name)
    add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)
