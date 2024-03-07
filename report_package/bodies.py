from reportlab.platypus import Paragraph, PageBreak
from report_package import styles, tools

img_file_exts = ["png", "jpg", "jpeg", "gif"]
table_file_exts = ["xlsx", "csv"]
txt_file_exts = ["txt"]

def create(content, data):
    for chapter in data:
        chapter_num = chapter[7:]
        content.append(Paragraph(styles.bold(chapter_num + ". "+ data[chapter]["Title"]), styles.h2))
        content.append(styles.h1_spacer)
        for section_num in data[chapter]["Sections"]:
            section = data[chapter]["Sections"][section_num]
            content.append(Paragraph(styles.bold("&nbsp;&nbsp;" + chapter_num + "." + section_num + ". " + section["Title"]), styles.h3))
            content.append(styles.h2_spacer)
            
            for c in section["Contents"]:
                file = c.split("/")[-1]
                try:
                    if file.split(".")[-1].lower() in txt_file_exts:
                        tools.insert_text_file(c, content)
                    elif file.split(".")[-1].lower() in img_file_exts:
                        tools.insert_image_file(c, content, 0.6)
                    elif file.split(".")[-1].lower() in table_file_exts:
                        tools.insert_excel_to_table(c, content)
                    else :
                        print(file + " Is Not Supported!")
                        content.append(Paragraph(styles.bold(file + " Is Not Supported")))
                except FileNotFoundError:  
                    print(file + " Is Not Found!")
                    content.append(Paragraph(styles.bold(file + " Is Not Found!")))
                
            content.append(PageBreak())