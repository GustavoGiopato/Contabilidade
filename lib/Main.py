import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry



class LancamentoContabil:
    def __init__(self,data, conta_debito, conta_credito, valor, historico):
        self.data = data
        self.conta_debito = conta_debito
        self.conta_credito = conta_credito
        self.valor = valor
        self.historico = historico


class LivroDiario:
    def __init__(self):
        self.lancamentos = []

    def adicionar_lancamento(self, lancamento):
        self.lancamentos.append(lancamento)

    def mostrar_livro_diario(self):
        livro_diario_texto = "Livro Diário:\n\n"
        for lancamento in self.lancamentos:
            livro_diario_texto += f"Data: {lancamento.data}\n"
            livro_diario_texto += f"Conta Débito: {lancamento.conta_debito}\n"
            livro_diario_texto += f"Conta Crédito: {lancamento.conta_credito}\n"
            livro_diario_texto += f"Valor: {lancamento.valor}\n"
            livro_diario_texto += f"Histórico: {lancamento.historico}\n"
            livro_diario_texto += "-----\n"

        return livro_diario_texto

def adicionar_lancamento():
    conta_debito = var_conta_debito.get()
    conta_credito = var_conta_credito.get()
    valor = float(entry_valor.get())
    historico = entry_historico.get()
    data = entry_data.get_date()  # Obter a data selecionada pelo usuário
    lancamento = LancamentoContabil(data, conta_debito, conta_credito, valor, historico)

    livro_diario.adicionar_lancamento(lancamento)

def exibir_livro_diario():
    livro_diario_texto = livro_diario.mostrar_livro_diario()
    messagebox.showinfo("Livro Diário", livro_diario_texto)

# Criação do livro diário
livro_diario = LivroDiario()

# Criação da janela principal
janela = tk.Tk()
janela.title("Livro Diário")

# Labels
label_data = tk.Label(janela, text="Data:")
label_data.pack()
entry_data = DateEntry(janela, date_pattern="dd/mm/yyyy", width=12, background='darkblue', foreground='white', borderwidth=2)
entry_data.pack()
contas_debito = ["Conta A", "Conta B", "Conta C"]
contas_credito = ["Conta X", "Conta Y", "Conta Z"]
label_conta_debito = tk.Label(janela, text="Conta Débito:")
label_conta_debito.pack()
var_conta_debito = tk.StringVar()
dropdown_conta_debito = tk.OptionMenu(janela, var_conta_debito, *contas_debito)
dropdown_conta_debito.pack()

label_conta_credito = tk.Label(janela, text="Conta Crédito:")
label_conta_credito.pack()
var_conta_credito = tk.StringVar()
dropdown_conta_credito = tk.OptionMenu(janela, var_conta_credito, *contas_credito)
dropdown_conta_credito.pack()
label_valor = tk.Label(janela, text="Valor:")
label_valor.pack()
entry_valor = tk.Entry(janela)
entry_valor.pack()
label_historico = tk.Label(janela, text="Histórico:")
label_historico.pack()
entry_historico = tk.Entry(janela)
entry_historico.pack()

# Botões
botao_adicionar = tk.Button(janela, text="Adicionar Lançamento", command=adicionar_lancamento)
botao_adicionar.pack()

botao_exibir = tk.Button(janela, text="Exibir Livro Diário", command=exibir_livro_diario)
botao_exibir.pack()

# Executar a janela principal
janela.mainloop()
