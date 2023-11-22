import openpyxl

book = openpyxl.load_workbook("responses.xlsx")

sheet = book.active

for row in sheet.rows:
    if(row[1].value != None):                   #for cleaning numbers
        a = row[1].value
        b = "+" + a[1:5] + "***" + a[8:]
        row[1].value = b
    
    if(row[2].value != None):
        c = row[2].value
        name = "GAIA A."                        #put the name here
        if name in c:
            d = c.replace(name, "<REAL NAME>")
            row[2].value = d

book.save('responses.xlsx')