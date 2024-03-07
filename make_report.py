import json
import sys
from report_package import cover, proj_info, table_of_contents, bodies, closing
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from report_package import styles

report_type = ""

def main():
    with open("/lustre2/BI_Analysis/pilkyu/Creating_Report_PDF/config.json", "r") as config:
        data = json.load(config)[report_type]
        
        title_name = data["Cover"]["Name"] + " Report"
        pdf = SimpleDocTemplate(data["Save_Location"] + "/" + data["Cover"]["Name"] + ".pdf", title=title_name, pagesize=A4)
        content = []
        cover.create(content, data["Cover"])
        proj_info.create(content, data["Project Information"])
        table_of_contents.create(content, data["Body"])
        bodies.create(content, data["Body"])
        closing.create(content)

        pdf.build(content, onFirstPage=styles.first_page, onLaterPages=styles.later_pages)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        report_type = sys.argv[1]
        main()
    else:
        print("USAGE: make_report.py \"REPORT TYPE\"")
        exit()
