import openpyxl
import random

book = openpyxl.load_workbook("spam data.xlsx")

sheet = book.active

for row in sheet.rows:
    # if(row[2].value != None):                   #for cleaning numbers
    #     a = str(row[2].value)
    #     b = "+" + a[0:4] + "***" + a[7:]
    #     row[2].value = b

    # if(row[1].value != None):                   #for cleaning numbers
    #     a = str(row[1].value)
    #     if a[0:2] == "++":
    #         b = a[1:]
    #         row[1].value = b

    # if(row[1].value != None):                   #for cleaning numbers
    #     a = str(row[1].value)
    #     if(a[4:8] == "****"):
    #         b = a[0:4] + str(random.randint(0, 9)) + "***" + a[8:]
    #         row[1].value = b

    if(row[2].value != None):
        c = row[2].value
        names = ["<REAL NAME>", "ANN BEATRICE D.", "KRIZTAL HOPE T.", "KURTNEY U.", "<recipient name>", "DARAH VIA D. M.", "GWYNETH ANNE L.","Jhon N.","JUNEVI B.","ANNE BEATRICE D.","KYLE E.","ARMEL SIEAN E.","JUSTINE C.", "JO-ANN J.","MICHAEL PATRICK P.","MICHAEL PATRICK P","RUSSEL JADE T.","JOSE MIGUEL G.", "FENNIE MAE T.","DIVINE GRACE L."]
        
        for name in names:
            if name in c:
                d = c.replace(name, "JUAN C.")
                row[2].value = d
                break

    # if(row[2].value != None):                               #to remove whitespace in numbers                                       
    #     row[2].value = str(row[2].value).replace(' ','')

book.save('spam data.xlsx')
