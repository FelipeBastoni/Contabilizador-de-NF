from tkinter import filedialog
import shutil
import os


def incluir_arquivo(formato):


    if formato == "P":

        PASTA_DESTINO = "Notas"


        arquivos = filedialog.askopenfilenames(
            title="Incluir arquivos",
            filetypes=[("Todos os arquivos", "*.*")]
        )

        if not arquivos:
            return

        os.makedirs(PASTA_DESTINO, exist_ok=True)

        copiados = 0

        for arquivo in arquivos:
            nome = os.path.basename(arquivo)
            destino = os.path.join(PASTA_DESTINO, nome)

            
            if not os.path.exists(destino):
                shutil.copy(arquivo, destino)
                copiados += 1


        return True

    if formato == "X":

        PASTA_DESTINO = "Xml"


        arquivos = filedialog.askopenfilenames(
            title="Incluir arquivos",
            filetypes=[("Todos os arquivos", "*.*")]
        )

        if not arquivos:
            return

        os.makedirs(PASTA_DESTINO, exist_ok=True)

        copiados = 0

        for arquivo in arquivos:
            nome = os.path.basename(arquivo)
            destino = os.path.join(PASTA_DESTINO, nome)

            
            if not os.path.exists(destino):
                shutil.copy(arquivo, destino)
                copiados += 1



    return True