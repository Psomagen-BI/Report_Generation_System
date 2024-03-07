from reportlab.platypus import Paragraph, PageBreak
from report_package import styles as Styles, tools as Tools
from reportlab.platypus import Spacer
from reportlab.lib.units import cm
from report_package import styles

def create(content, data):
    content.append(Paragraph(styles.bold("Project Information"), Styles.h1))
    content.append(Spacer(1.5*cm, 1.5*cm))

    content.append(Tools.make_table(data))
    content.append(PageBreak())
    