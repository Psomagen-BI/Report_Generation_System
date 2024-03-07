from report_package import tools
from reportlab.platypus import Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

def create(content):
    path = "/lustre2/BI_Analysis/pilkyu/Creating_Report_PDF/sources/Closing_Page.png"
    content.append(Spacer(3*cm, 3*cm))
    tools.insert_image_file(path, content, 0.9)