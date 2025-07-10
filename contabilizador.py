import fitz 
import pandas as pd
import os



def proceed():

    db = pd.read_excel("dbxlsx.xlsx", sheet_name="Faturamento")


    valordb = db.loc[db["Produto"] == "$"+prod, "Valor"].values[0]
    nv_valor = valordb + valor

    db.loc[db['Produto'] == "$"+prod, 'Valor'] = nv_valor



    quantdb = db.loc[db["Produto"] == "$"+prod, "Unidades"].values[0]
    nv_quant = quantdb + quant

    db.loc[db['Produto'] == "$"+prod, 'Unidades'] = nv_quant



    with pd.ExcelWriter("dbxlsx.xlsx", engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        db.to_excel(writer, sheet_name="Faturamento", index=False)



n = 1
nfim = 327
i = 0


while i == 0:

    pdf = (f'NF{n}.pdf')

    if n != (nfim + 1):

        if os.path.exists(pdf):

            with fitz.open(f"NF{n}.pdf") as pdf:
                for pagina in pdf:
                    texto = pagina.get_text()

            with open("Nf.txt", "w", encoding="utf-8") as saidatxt:
                saidatxt.write(texto)

                for index, linha in enumerate(texto.splitlines()):

                    if "789" in linha:
            
                        sku = index
                        uni = index + 5
                        preco = index + 7

                        prod = texto.splitlines()[sku].split()[0]
                        print(prod)
                        quant = int(texto.splitlines()[uni].split()[0])
                        print(quant)
                        valor = float((texto.splitlines()[preco].replace(".", "")).replace(",", "."))
                        print(valor)
                        NF = texto.splitlines()[34].split()[0]
                    

                        proceed()


            print("Um arquivo finalizado " + NF)

            db = pd.read_excel("dbxlsx.xlsx", sheet_name="Faturamento")

            vendas = db.loc[db["Unidades"] == "Total", "Vendas"].values[0]
            vendas = vendas + 1

            db.loc[db["Unidades"] == "Total", "Vendas"] = vendas



            with pd.ExcelWriter("dbxlsx.xlsx", engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                db.to_excel(writer, sheet_name="Faturamento", index=False)
    

            n = n + 1


        else:
            
            n = n + 1

    else:

        i = 1