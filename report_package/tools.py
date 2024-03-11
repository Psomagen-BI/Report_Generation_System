from reportlab.platypus import Table, Paragraph, Image
from report_package import styles
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import pandas as pd
import csv
import numpy as np

def insert_text_file(path, content):
    with open(path, "r") as file:
        text_file = file.read()
        ps = text_file.split('\n')
        for p in ps:
            if len(p) != 0:
                content.append(Paragraph(styles.tab + p, styles.h4))
                content.append(styles.h4_spacer)

def insert_image_file(path, content, rate):
    img_reader = ImageReader(path)
    width = img_reader.getSize()[0]
    height = img_reader.getSize()[1]
    if width > height:
        ratio = width / A4[0]
        width /= ratio
        height /= ratio
    else :
        ratio = height / A4[1]
        width /= ratio
        height /= ratio

    img = Image(path, width = width*rate, height=height*rate)
    content.append(img)
    content.append(styles.h4_spacer)

def insert_excel_to_table(path, page):
    ext = path.split("/")[-1].split(".")[-1]
    arr = []

    if ext == "csv":
        with open(path, mode='r') as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                arr.append(line)
    elif ext == "xlsx":
        df = pd.read_excel(path, header=None, engine="openpyxl")
        df = df.replace(r'^\s+$', np.nan, regex=True).dropna(how='all')
        arr = df.values.tolist()

    if page == "proj_info":
        styles.proj_info_table_paragraphize(arr)
    else:
        styles.content_table_paragraphize(arr)

    t = Table(arr)
    return t