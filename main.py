""" Merge PDF Files using python
I got tired of Adobe's paywall to process my pdf files
so I looked up how to do it in python"""

from PyPDF4 import PdfFileMerger

merger = PdfFileMerger()

pdf_files = ['img001.pdf', 'img002.pdf', 'img003.pdf', 'img004.pdf', 'img005.pdf']

for file in pdf_files:
    merger.append(file)

merger.write("My_ocie.pdf")
merger.close()
