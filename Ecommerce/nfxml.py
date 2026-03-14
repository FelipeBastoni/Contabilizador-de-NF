import xml.etree.ElementTree as ET
import pandas as pd 
import os

pasta = "Xml"

for xml in os.listdir(pasta):

    caminho = os.path.join(pasta, xml)

    tree = ET.parse(caminho)
    root = tree.getroot()

    ns = {"nfe": "http://www.portalfiscal.inf.br/nfe"}

    print(xml)

    def computxml():

        db = pd.read_excel("C:/Users/proje/OneDrive/Documentos/dbxlsx.xlsx", sheet_name="Faturamento")

        
        db[["Valor", "Unidades", "Num. Vendas"]] = 0

        db.loc[0,"Total"] = 0

        with pd.ExcelWriter("C:/Users/proje/OneDrive/Documentos/dbxlsx.xlsx", engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            db.to_excel(writer, sheet_name="Faturamento", index=False)



        def proceed():

            
            valordb = db.loc[db["Produto"] == "$"+cProd, "Valor"].values[0]
            nv_valor = valordb + vProd

            db.loc[db['Produto'] == "$"+cProd, 'Valor'] = nv_valor



            quantdb = db.loc[db["Produto"] == "$"+cProd, "Unidades"].values[0]
            nv_quant = quantdb + qCom

            db.loc[db['Produto'] == "$"+cProd, 'Unidades'] = nv_quant



            nmvendasdb = db.loc[db["Produto"] == "$"+cProd, "Num. Vendas"].values[0]
            nv_nmvd = nmvendasdb + 1

            db.loc[db['Produto'] == "$"+cProd, 'Num. Vendas'] = nv_nmvd


            with pd.ExcelWriter("C:/Users/proje/OneDrive/Documentos/dbxlsx.xlsx", engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                db.to_excel(writer, sheet_name="Faturamento", index=False)




        for det in root.findall(".//nfe:det", ns):

            prod = det.find("nfe:prod", ns)

            cProd = prod.find("nfe:cProd", ns).text
            vProd = float(prod.find("nfe:vProd", ns).text)
            qCom = float(prod.find("nfe:qCom", ns).text)

            print(cProd, vProd, qCom)
            print("\n")

            proceed()

