import datetime
from reportlab.platypus import Paragraph, PageBreak
from reportlab.platypus import Spacer
from reportlab.lib.units import cm
from report_package import styles

def create(content):
    month_year = datetime.datetime.now().strftime("%B %Y")
    
    content.append(Spacer(3*cm, 3*cm))
    content.append(Paragraph(styles.bold("Report"), styles.cover_h1))
    content.append(Spacer(4*cm, 4*cm))
    content.append(Paragraph(styles.bold(month_year), styles.cover_date))

    content.append(PageBreak())