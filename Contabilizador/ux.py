import tkinter as tk
from ecommerce import comput
from inclusao  import incluir_arquivo

j = tk.Tk()
j.title("Contabilizador de Vendas") 
j.geometry = ("1100x600")
j.minsize(1100, 600)
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
    bt2.place_forget()
    bt3.place_forget()
    ent1.place_forget()
    ent2.place_forget()
    ent3.place_forget()



def inc():

    forget()

    txt3.place(x=20, y=30)
    txt4.place(x=20, y=60)
    txt5.place(x=20, y=90)
    bt2.place(x=20, y=150)
    txt6.place(x=20, y=210)




def rel():

    forget()

    txt7.place(x=20, y=30)
    txt8.place(x=20, y=90)
    txt9.place(x=260, y=90)
    ent1.place(x=20, y=120)
    ent2.place(x=260, y=120)
    txt10.place(x=20, y=180)
    ent3.place(x=20, y=210)
    bt3.place(x=450, y=240)
    txt11.place(x=20, y=280)




def alt():

    forget()





#funcionalidades


def incluir():

    alert = incluir_arquivo()

    if alert == True:

        txt6.config(text="Arquivos incluidos com sucesso")



def gerar_relatorio():

    nf_i = int(ent1.get())
    nf_f = int(ent2.get())
    loc = ent3.get()



    if nf_f < nf_i:

        txt11.config(text="Status: O número da NF final tem que ser maior que o número da NF inicial")
        
        return



    alert = comput(nf_i, nf_f, loc)

    if alert == True:

        txt11.config(text="Status: Processo Finalizado")

    else:

        txt11.config(text="Status: Processo Falhou")





#menu lateral

frm1 = tk.Frame(j, bg="gray")
frm1.place(x=0, y=0, width=500, height=800)

txt1 = tk.Label(frm1, text="Seja bem vindo ao Contabilizador de NF's")
txt1.place(x=20, y=30)

txt2 = tk.Label(frm1, text="O que você deseja fazer?")
txt2.place(x=20, y=60)

bt1 = tk.Button(frm1, text="Adicionar NF's", width=15, command=inc)
bt1.place(x=20, y=130)

bt1 = tk.Button(frm1, text="Tirar Relatórios", width=15, command=rel)
bt1.place(x=20, y=160)



bt99 = tk.Button(frm1, text="Voltar", width=15, command=alt)
bt99.place(relx=0.15, rely=0.72, anchor="s")



#tela main

frm2 = tk.Frame(j, bg="#FDFFEE")
frm2.place(relx=150/600, rely=0, relwidth=600, relheight=1)




#tela de inclusão de NF's

txt3 = tk.Label(frm2, text="Selecione as NF's que você deseja incluir")

txt4 = tk.Label(frm2, text="Não se esqueça de renomear os arquivos como: NF'Número da NF' apenas, e os mesmos devem ser PDF")

txt5 = tk.Label(frm2, text="Se isso não for feito o arquivo não será lido")

bt2 = tk.Button(frm2, text="Incluir", command=incluir)

txt6 = tk.Label(frm2)


#tela de Relatórios

txt7 = tk.Label(frm2, text="Selecione a NF de início e a NF de fim")

txt8 = tk.Label(frm2, text="NF início:")

txt9 = tk.Label(frm2, text="NF fim:")

ent1 = tk.Entry(frm2, width=25)

ent2 = tk.Entry(frm2, width=25)

txt10 = tk.Label(frm2, text="Selecione o local (deixe em branco se não tiver algum específico)")

ent3 = tk.Entry(frm2)

bt3 = tk.Button(frm2, text="Gerar relatório", command=gerar_relatorio)

txt11 = tk.Label(frm2, text="Status: ")





j.mainloop()