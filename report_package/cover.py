from reportlab.platypus import Paragraph, PageBreak
from reportlab.platypus import Spacer
from reportlab.lib.units import cm
from report_package import styles

def create(content, data):
    content.append(Spacer(2.5*cm, 2.5*cm))
    content.append(Paragraph(data["Name"], styles.cover_h1))
    content.append(Spacer(1*cm, 1*cm))
    content.append(Paragraph(styles.bold("Report"), styles.cover_h1))
    content.append(Spacer(2*cm, 2*cm))
    content.append(Paragraph(styles.bold(data["Date"]), styles.cover_date))

    content.append(PageBreak())