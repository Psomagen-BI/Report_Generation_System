import os
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import Spacer, TableStyle, Paragraph

# Cover Page Style
def first_page(canvas, pdf):
    canvas.saveState()
    back_image_path = os.path.join("sources", "Cover_Image.png")
    psom_image_path = os.path.join("sources", "psoma_logo_whiteback.PNG")
    back_image = ImageReader(back_image_path)
    psom_image = ImageReader(psom_image_path)
    canvas.drawImage(back_image, 0, pdf.height/5, pdf.width+150, pdf.height*3/5)
    canvas.drawString(50, 50, "Copyright \u00A9 Psomagen, Inc")
    canvas.drawImage(psom_image, canvas._pagesize[0] - 200, 50, 170, 50)
    canvas.restoreState()

# All Pages Except the First Page
def later_pages(canvas, doc):
    canvas.saveState()
    # Upper Right Image
    psom_image_path = os.path.join("sources", "psoma_logo_whiteback.PNG")
    psom_image = ImageReader(psom_image_path)
    canvas.drawImage(psom_image, canvas._pagesize[0] - 150, canvas._pagesize[1] - 60, 110, 40)
    # Bottom Right Page Number
    canvas.setFont("Helvetica", 14)
    canvas.drawString(canvas._pagesize[0] - 70, 40, "%d"%(doc.page))
    # Bottom Center String
    canvas.setFont("Times-Roman", 8)
    canvas.drawString(canvas._pagesize[0]*2/5, 50, "PSOMAGEN NGS SERVICE")
    canvas.setFont("Times-Roman", 12)
    canvas.drawString(canvas._pagesize[0]*2/5, 36, "Research use only")
    canvas.restoreState()

def bold(str):
    return "<b>" + str + "</b>"

def proj_info_table_paragraphize(arr):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if col > 0:
                arr[row][col] = Paragraph(str(arr[row][col]), table_text_style)
            else:
                arr[row][col] = Paragraph(bold(str(arr[row][col])), table_text_style)
    
def content_table_paragraphize(arr):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if row > 0:
                arr[row][col] = Paragraph(str(arr[row][col]), table_text_style)
            else:
                arr[row][col] = Paragraph(bold(str(arr[row][col])), table_text_style)

cover_h1 = ParagraphStyle(
    name='cover_h1',
    parent=getSampleStyleSheet()['Normal'],
    fontSize=52,
    fontName='Times-Roman',
    leading=40
)

cover_date = ParagraphStyle(
    name='cover_date',
    parent=getSampleStyleSheet()['Normal'],
    fontSize=28,
    fontName='Times-Roman'
)

h0 = ParagraphStyle(
    name='h1',
    parent=getSampleStyleSheet()['Normal'],
    fontSize=28,
    fontName='Times-Roman'
)

h1 = ParagraphStyle(
    name='h1',
    parent=getSampleStyleSheet()['Normal'],
    fontSize=24,
    fontName='Times-Roman',
    leading=15
)

h1_spacer = Spacer(0.8*cm, 0.8*cm)

h2 = ParagraphStyle(
    name='h2',
    parent=getSampleStyleSheet()['Normal'],
    fontSize=20,
    fontName='Times-Roman',
    leading=15
)

h2_spacer = Spacer(0.5*cm, 0.5*cm)

h3 = ParagraphStyle(
    name='h3',
    parent=getSampleStyleSheet()['Normal'],
    fontSize=16,
    fontName='Times-Roman',
    leading=15
)
h3_spacer = Spacer(0.4*cm, 0.4*cm)

h4 = ParagraphStyle(
    name='h4',
    parent=getSampleStyleSheet()['Normal'],
    fontSize=12,
    fontName='Times-Roman',
    leading=14
)
h4_spacer = Spacer(0.3*cm, 0.3*cm)

tab = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"

table_text_style = ParagraphStyle(
    name='table_text',
    parent=getSampleStyleSheet()['Normal'],
    fontSize=10,
    fontName='Times-Roman',
    leading=14,
    alignment=1
)

proj_info_table_style = TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('LINEABOVE', (0,0), (-1,-1), 0.25, colors.black),
                        ('LINEBELOW', (0,0), (-1,-1), 0.25, colors.black),
                        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
                        ('FONT', (0, 0), (0, -1), 'Times-Bold'),
                        ('FONT', (1, 0), (1, -1), 'Times-Roman'),
                        ])

content_table_style = TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                        ('LINEBELOW', (0,0), (-1,-1), 0.25, colors.black),
                        ('FONT', (0, 0), (-1, 0), 'Times-Bold'),
                        ('FONT', (0, 1), (-1, -1), 'Times-Roman'),
                        ])