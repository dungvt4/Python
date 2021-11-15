import os
from docx import Document


doc = Document()
doc.add_heading("Resignation Letter")

save_path = os.path.dirname(os.path.abspath(__file__))
print(save_path)

file_name ='Resignation-Letter.docx'
print(os.path.join(save_path,"static",file_name))
# doc.save(os.path.join(save_path,'/static/',file_name))