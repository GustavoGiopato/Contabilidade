from Db import *
import tkinter

livro_diario = obter_livro_diario()
for registro in livro_diario:
    print(registro)