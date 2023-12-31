# -*- coding: utf-8 -*-
#CODED BY CWhide  20231231

from pdf2docx import Converter

pdf_file=r'test.pdf'
docx_file=r'test.docx'
Converter(pdf_file).convert(docx_file,start=0,end=None)
