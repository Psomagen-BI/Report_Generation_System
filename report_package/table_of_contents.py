from reportlab.platypus import Paragraph, PageBreak
from report_package import styles
from reportlab.platypus import Spacer, Image
from reportlab.lib.units import cm

def create(content, data):
    content.append(Paragraph(styles.bold("Table of Contents"), styles.h0))
    content.append(Spacer(0.7*cm, 0.7*cm))

    line_img_path = "/lustre2/BI_Analysis/pilkyu/Creating_Report_PDF/sources/line.png"
    line_img = Image(line_img_path, width=470)
    content.append(line_img)
    content.append(Spacer(0.3*cm, 0.3*cm))

    content.append(Paragraph(styles.bold("Project Information"), styles.h2))
    content.append(Spacer(1*cm, 1*cm))

    for chapter in data:
        chapter_num = chapter[7:]
        content.append(Paragraph(styles.bold(chapter_num + ". "+ data[chapter]["Title"]), styles.h2))
        content.append(Spacer(0.5*cm, 0.5*cm))

        for section_num in data[chapter]["Sections"]:
            section = data[chapter]["Sections"][section_num]
            content.append(Paragraph(styles.bold("&nbsp;&nbsp;&nbsp;&nbsp;" + chapter_num + "." + section_num + ". " + section["Title"]), styles.h4))
            content.append(Spacer(0.2*cm, 0.2*cm))

        content.append(Spacer(0.2*cm, 0.2*cm))
    content.append(PageBreak())
        