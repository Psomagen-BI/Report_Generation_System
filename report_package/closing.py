import os
from report_package import tools
from reportlab.platypus import Spacer
from reportlab.lib.units import cm

def create(content):
    img_path = os.path.join("sources", "Closing_Page.png")
    content.append(Spacer(3*cm, 3*cm))
    tools.insert_image_file(img_path, content, 0.9)