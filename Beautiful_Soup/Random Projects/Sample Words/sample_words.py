import pandas as pd
import pdfplumber
import json

# Find words to lookup 
template = pd.read_excel('Sample Words.xlsx')
lookup_dict = {}
for i in template[template.columns[0]][1:]:
    lookup_dict[i] = None
# print(lookup_dict)

# Processing pdf file into json to ease reading speed
pdf = pdfplumber.open('6.pdf')
pages = pdf.pages
pdf_dict = {}

# for word in lookup_dict.keys():
    # for index, page in enumerate(pages):
        # page_number = []
        # text = page.extract_text()
        # print(word)
        # if str(word) in str(text):
            # page_number.append(index+1)
    # lookup_dict[word] = page_number
    # pdf.close()
# print(lookup_dict)