#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
----------------------------------------------------------------------------------------------------
* Project Name : AddWatermark
* File Name    : clean_trash.py
* Description  : Clean all image and PDF files(including input and output)
* Create Time  : 2020-08-03 18:28:32
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh/AddWatermark
----------------------------------------------------------------------------------------------------
* Notice
-
-
----------------------------------------------------------------------------------------------------
'''


import os


def clean():
    '''Delete image and PDF files'''

    print('⚠️此脚本按文件后缀匹配, 会删除当前目录所有匹配后缀的文件')
    del_formats = input('要删除的格式(默认删除pdf, jpg, png)\ne.g. pdf jpg png:\n>>> ').split()

    if del_formats:
        for fmt in del_formats:
            os.system(f'rm *.{fmt}')
    else:
        os.system('rm *.pdf')
        os.system('rm *.jpg')
        os.system('rm *.png')


if __name__ == "__main__":
    clean()
