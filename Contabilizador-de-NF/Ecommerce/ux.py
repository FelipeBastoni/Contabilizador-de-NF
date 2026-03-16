import tkinter as tk
from nfpdf import comput
from nfxml import init
from inclusao  import incluir_arquivo

j = tk.Tk()
j.title("Contabilizador de Vendas") 
j.geometry = ("1100x600")
j.minsize(1300, 800)
j.resizable(False, False)



#manipulações da interface


def forget():

    txt3.place_forget()
    txt4.place_forget()
    txt5.place_forget()
    txt6.place_forget()
    txt7.place_forget()
    txt8.place_forget()
    txt9.place_forget()
    txt10.place_forget()
    txt11.place_forget()
    txt12.place_forget()
    txt13.place_forget()
    txt14.place_forget()
    txtdt1.place_forget()
    txtdt2.place_forget()
    txtdt3.place_forget()
    txtbase.place_forget()
    btl.place_forget()
    bt2.place_forget()
    bt3.place_forget()
    bt4.place_forget()
    btxml.place_forget()
    btpdf.place_forget()
    btvolt_inc.place_forget()
    dtbxml.place_forget()
    dtbpdf.place_forget()
    btrel_volt.place_forget()
    selctdt.place_forget()
    selctnf.place_forget()
    selctall.place_forget()
    ent1.place_forget()
    ent2.place_forget()
    ent3.place_forget()

    ent1.delete(0, 'end')
    ent2.delete(0, 'end')
    ent3.delete(0, 'end')



def inc():

    forget()

    txt3.place(x=20, y=30)
    btxml.place(x=20, y=60)
    btpdf.place(x=120, y=60)

def inc_pdf():

    forget()

    txt4.place(x=20, y=30)
    txt5.place(x=20, y=60)
    bt2.place(x=20, y=90)
    txt6.place(x=20, y=150)
    btvolt_inc.place(x=20, y=250)


def inc_xml():

    forget()

    txt13.place(x=20, y=30)
    bt4.place(x=20, y=90)
    txt6.place(x=20, y=150)
    btvolt_inc.place(x=20, y=250)




def rel():

    forget()

    txtbase.place(x=20, y=30)
    dtbxml.place(x=20, y=60)
    dtbpdf.place(x=170, y=60)


def dbxml():

    forget()

    txt14.place(x=20, y=30)
    selctall.place(x=20, y=60)
    txt12.place(x=20, y=120)
    btrel_volt.place(x=20, y=190)


def dbpdf():

    forget()

    txt7.place(x=20, y=30)
    selctdt.place(x=20, y=60)
    selctnf.place(x=200, y=60)
    btrel_volt.place(x=20, y=160)
    

def data():

    forget()

    txt7.place(x=20, y=30)
    selctdt.place(x=20, y=60)
    selctnf.place(x=200, y=60)

    txtdt1.place(x=20, y=120)
    txtdt2.place(x=20, y=150)
    txtdt3.place(x=260, y=150)
    ent1.place(x=20, y=180)
    ent2.place(x=260, y=180)
    txt11.place(x=20, y=210)
    ent3.place(x=20, y=240)
    bt3.place(x=450, y=270)
    txt12.place(x=20, y=300)
    btrel_volt.place(x=20, y=400)



def nota():

    forget()

    txt7.place(x=20, y=30)
    selctdt.place(x=20, y=60)
    selctnf.place(x=200, y=60)

    txt8.place(x=20, y=120)
    txt10.place(x=260, y=150)
    txt9.place(x=20, y=150)
    ent1.place(x=20, y=180)
    ent2.place(x=260, y=180)
    txt11.place(x=20, y=210)
    ent3.place(x=20, y=240)
    bt3.place(x=450, y=270)
    txt12.place(x=20, y=300)
    btrel_volt.place(x=20, y=400)




def alt():

    forget()





#funcionalidades


def incluir(formato):

    alert = incluir_arquivo(formato)

    if alert == True:

        txt6.config(text="Arquivos incluidos com sucesso")



def gerar_relatorio():

    nf_i = int(ent1.get())
    nf_f = int(ent2.get())
    loc = ent3.get()



    if nf_f < nf_i:

        txt12.config(text="Status: O número da NF final tem que ser maior que o número da NF inicial")
        
        return



    alert = comput(nf_i, nf_f, loc)

    if alert == True:

        txt12.config(text="Status: Processo Finalizado")

    else:

        txt12.config(text="Status: Processo Falhou")








#menu lateral

frm1 = tk.Frame(j, bg="gray")
frm1.place(x=0, y=0, width=700, height=800)

txt1 = tk.Label(frm1, text="Seja bem vindo ao Contabilizador de NF's")
txt1.place(x=20, y=30)

txt2 = tk.Label(frm1, text="O que você deseja fazer?")
txt2.place(x=20, y=60)

bt1 = tk.Button(frm1, text="Adicionar NF's", width=15, command=inc)
bt1.place(x=20, y=130)

bt1 = tk.Button(frm1, text="Gerar Relatórios", width=15, command=rel)
bt1.place(x=20, y=160)

btl = tk.Button(frm1, text="Lista de Produtos", width=15, command=rel)
btl.place(x=20, y=190)


bt99 = tk.Button(frm1, text="Voltar", width=15, command=alt)
bt99.place(relx=0.15, rely=0.95, anchor="s")



#tela main

frm2 = tk.Frame(j, bg="#FDFFEE")
frm2.place(relx=150/600, rely=0, relwidth=600, relheight=1)




#tela de inclusão de NF's

txt3 = tk.Label(frm2, text="Selecione o formato de arquivo")

btxml = tk.Button(frm2, text="XML", command=inc_xml)

btpdf = tk.Button(frm2, text="PDF", command=inc_pdf)

btvolt_inc = tk.Button(frm2, text="Voltar", command=inc)


#por PDF

txt4 = tk.Label(frm2, text="Não se esqueça de renomear os arquivos como: NF'Número da NF' apenas, e os mesmos devem ser PDF")

txt5 = tk.Label(frm2, text="Se isso não for feito o arquivo não será lido")

bt2 = tk.Button(frm2, text="Incluir", command=lambda: incluir("P"))

txt6 = tk.Label(frm2)


#por XML

txt13 = tk.Label(frm2, text="Clique no boão para selecionar os arquivos")

bt4 = tk.Button(frm2, text="Incluir", command=lambda: incluir("X"))


#aviso

txt6 = tk.Label(frm2)




#tela de Relatórios

txtbase = tk.Label(frm2, text="Qual base de dados você deseja utilizar?")

dtbxml = tk.Button(frm2, text="XML", command=dbxml)

dtbpdf = tk.Button(frm2, text="PDF", command=dbpdf)


#Seleção de base de dados

txt7 = tk.Label(frm2, text="Como você deseja filtrar")

selctdt = tk.Button(frm2, width=15, text="Data", command=data)

selctnf = tk.Button(frm2, width=15, text="Nota Fiscal", command=nota)


#PDF

#por data

txtdt1 = tk.Label(frm2, text="Selecione a data de início e a data de fim")

txtdt2 = tk.Label(frm2, text="Data inicial:")

txtdt3 = tk.Label(frm2, text="Data Final:")


#por nota fiscal


txt8 = tk.Label(frm2, text="Selecione a NF de início e a NF de fim")

txt9 = tk.Label(frm2, text="NF início:")

txt10 = tk.Label(frm2, text="NF fim:")

ent1 = tk.Entry(frm2, width=25)

ent2 = tk.Entry(frm2, width=25)

txt11 = tk.Label(frm2, text="Selecione o local (deixe em branco se não tiver algum específico)")

ent3 = tk.Entry(frm2)

bt3 = tk.Button(frm2, text="Gerar relatório", command=gerar_relatorio)



#XML

txt14 = tk.Label(frm2, text="selecione como você deseja filtrar")

selctall = tk.Button(frm2, width=15, text="Todas", command=init)




#Status

txt12 = tk.Label(frm2, text="Status: ")


#Botão de retorno

btrel_volt = tk.Button(frm2, text="Voltar", command=rel)


j.mainloop()