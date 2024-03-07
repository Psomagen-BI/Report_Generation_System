from reportlab.platypus import Table, TableStyle, Paragraph, Image
from reportlab.lib import colors
from report_package import styles
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import pandas as pd
import csv

def make_table(data):
    pre_table = []
    for k in data:
        arr = []
        arr.append(k)
        arr.append(data[k])
        pre_table.append(arr)

    t=Table(pre_table, colWidths=[170, 330])
    t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('LINEABOVE', (0,0), (-1,-1), 0.25, colors.black),
                        ('LINEBELOW', (0,0), (-1,-1), 0.25, colors.black),
                        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
                        ('FONT', (0, 0), (0, -1), 'Times-Bold'),
                        ('FONT', (1, 0), (1, -1), 'Times-Roman'),
                        ]))
    return t

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

def insert_excel_to_table(path, content):
    ext = path.split("/")[-1].split(".")[-1]
    arr = []

    if ext == "csv":
        with open(path, mode='r') as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                arr.append(line)
    elif ext == "xlsx":
        df = pd.read_excel(path, header=None, engine="openpyxl")
        arr = df.values.tolist()

    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if row > 0:
                arr[row][col] = Paragraph(str(arr[row][col]), styles.table_text_style)

    t=Table(arr)
    t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                        ('LINEBELOW', (0,0), (-1,-1), 0.25, colors.black),
                        ('FONT', (0, 0), (-1, 0), 'Times-Bold'),
                        ('FONT', (0, 1), (-1, -1), 'Times-Roman'),
                        ]))

    content.append(t)
    content.append(styles.h4_spacer)