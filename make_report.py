import json
import os
from report_package import cover, proj_info, table_of_contents, bodies, closing
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from report_package import styles

def main():
    path = os.path.dirname(__file__)
    config_path = os.path.join(path, "config.json")

    with open(config_path, "r") as config:
        data = json.load(config)
        
        title_name = "Report"
        pdf = SimpleDocTemplate(os.path.join(path, "Report.pdf"), title=title_name, pagesize=A4)
        content = []
        cover.create(content)
        proj_info.create(content)
        table_of_contents.create(content, data)
        bodies.create(content, data)
        closing.create(content)

        pdf.build(content, onFirstPage=styles.first_page, onLaterPages=styles.later_pages)

if __name__ == "__main__":
    main()
