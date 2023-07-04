from Db import *
import tkinter as tk


class LivroDiarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Livro Diário")
        
        # Criação dos elementos da interface
        self.label = tk.Label(root, text="Dados do Livro Diário")
        self.label.pack()
        
        self.listbox = tk.Listbox(root)
        self.listbox.pack()
        
        self.button = tk.Button(root, text="Atualizar", command=self.atualizar_livro_diario)
        self.button.pack()
        
        # Conexão com o banco de dados
        self.connection, self.cursor = create_connection()
        
        # Atualiza os dados do Livro Diário
        self.atualizar_livro_diario()
    
    def atualizar_livro_diario(self):
        # Obtém os dados do Livro Diário do banco de dados
        livro_diario = obter_livro_diario(self.connection, self.cursor)
        
        # Limpa a listbox
        self.listbox.delete(0, tk.END)
        
        # Preenche a listbox com os dados obtidos
        for registro in livro_diario:
            self.listbox.insert(tk.END, str(registro))
        
if __name__ == "__main__":
    root = tk.Tk()
    app = LivroDiarioApp(root)
    root.mainloop()

connection, cursor = create_connection()

livro_diario = obter_livro_diario(connection, cursor)


for registro in livro_diario:
    print(registro)

cursor.close()
connection.close()
