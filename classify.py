import openpyxl
import random

book = openpyxl.load_workbook("test.xlsx")

sheet = book.active
count = 0

for row in sheet.rows:
    # if(row[2].value == "Spam"):
    #     msg = row[1].value
    #     keywords = ["JUAN C.", "Bank", ".com", "link"]
        
    #     for keyword in keywords:
    #         if keyword in msg:
    #             row[4].value = "1"
    #             break
    # else:
    #     row[4].value = "0"

    if(row[4].value == "-"):
        count += 1
    
print(count)        
book.save('test.xlsx')
