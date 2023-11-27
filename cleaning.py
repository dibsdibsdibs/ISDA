import openpyxl

book = openpyxl.load_workbook("responses.xlsx")

sheet = book.active

for row in sheet.rows:
    if(row[1].value != None):                   #for cleaning numbers
        a = str(row[1].value)
        b = "+" + a[0:4] + "***" + a[7:]
        row[1].value = b

    # if(row[2].value != None):
    #     c = row[2].value
    #     name = "<REAL NAME>"                        #put the name here
    #     if name in c:
    #         d = c.replace(name, "JUAN C.")
    #         row[2].value = d

    # if(row[1].value != None):                               #to remove whitespace in numbers                                       
    #     row[1].value = str(row[1].value).replace(' ','')

book.save('responses.xlsx')