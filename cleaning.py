import openpyxl

book = openpyxl.load_workbook("responses.xlsx")

sheet = book.active

for row in sheet.rows:
    # if(row[1].value != None):                   #for cleaning numbers
    #     a = str(row[1].value)
    #     b = "+" + a[0:4] + "***" + a[7:]
    #     row[1].value = b

    if(row[2].value != None):
        c = row[2].value
        names = ["ANN BEATRICE D.", "KRIZTAL HOPE T.", "KURTNEY U.", "<recipient name>", "DARAH VIA D. M.", "GWYNETH ANNE L.","Jhon N.","JUNEVI B.","ANNE BEATRICE D.","KYLE E.","ARMEL SIEAN E.","JUSTINE C.", "JO-ANN J.","MICHAEL PATRICK P.","MICHAEL PATRICK P","RUSSEL JADE T.","JOSE MIGUEL G.", "FENNIE MAE T.","DIVINE GRACE L."]
        
        for name in names:
            if name in c:
                d = c.replace(name, "JUAN C.")
                row[2].value = d
                break

    # if(row[1].value != None):                               #to remove whitespace in numbers                                       
    #     row[1].value = str(row[1].value).replace(' ','')

book.save('responses.xlsx')