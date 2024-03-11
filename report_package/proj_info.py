import os
from reportlab.platypus import Paragraph, PageBreak
from report_package import styles, tools
from reportlab.platypus import Spacer
from reportlab.lib.units import cm

def create(content):
    content.append(Paragraph(styles.bold("Project Information"), styles.h1))
    content.append(Spacer(1.5*cm, 1.5*cm))
    table_path = os.path.join("Project_Information", "Project_Info_Table.xlsx")
    table = tools.insert_excel_to_table(table_path, "proj_info")
    table.setStyle(styles.proj_info_table_style)

    content.append(table)
    content.append(PageBreak())
    