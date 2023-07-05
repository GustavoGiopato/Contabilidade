import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import tkinter.ttk as ttk
from ttkthemes import ThemedTk


class LancamentoContabil:
    def __init__(self, data, conta_debito, conta_credito, valor, historico):
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
        return self.lancamentos


def adicionar_lancamento():
    conta_debito = var_conta_debito.get()
    conta_credito = var_conta_credito.get()
    valor = float(entry_valor.get())
    historico = entry_historico.get()
    data = entry_data.get_date()
    lancamento = LancamentoContabil(data, conta_debito, conta_credito, valor, historico)
    livro_diario.adicionar_lancamento(lancamento)
    atualizar_tabela()


def atualizar_tabela():
    tabela.delete(*tabela.get_children())
    for lancamento in livro_diario.mostrar_livro_diario():
        tabela.insert("", "end", values=(
            lancamento.data.strftime("%d/%m/%Y"),
            lancamento.conta_debito,
            lancamento.conta_credito,
            lancamento.valor,
            lancamento.historico
        ))


# Criação do livro diário
livro_diario = LivroDiario()

# Criação da janela principal
janela = ThemedTk(theme="equilux", themebg=True)
janela.iconbitmap('lib\icon\icon.ico')
janela.title("Livro Diário")

# Labels
label_data = ttk.Label(janela, text="Data:")
label_data.grid(row=1, column=1, sticky="e")
entry_data = DateEntry(janela, date_pattern="dd/mm/yyyy", width=12, background='darkblue', foreground='white',
                       borderwidth=2)
entry_data.grid(row=1, column=2, sticky="w")

contas_debito = ["Conta A", "Conta B", "Conta C"]
contas_credito = ["Conta X", "Conta Y", "Conta Z"]

label_conta_debito = ttk.Label(janela, text="Conta Débito:")
label_conta_debito.grid(row=1, column=0, sticky="e")
var_conta_debito = tk.StringVar()
dropdown_conta_debito = ttk.OptionMenu(janela, var_conta_debito, *contas_debito)
dropdown_conta_debito.grid(row=1, column=1, sticky="w")

label_valor = ttk.Label(janela, text="Valor:")
label_valor.grid(row=1, column=2, sticky="e")
entry_valor = ttk.Entry(janela)
entry_valor.grid(row=1, column=3, sticky="we", padx=10)

label_conta_credito = ttk.Label(janela, text="Conta Crédito:")
label_conta_credito.grid(row=2, column=0, sticky="e")
var_conta_credito = tk.StringVar()
dropdown_conta_credito = ttk.OptionMenu(janela, var_conta_credito, *contas_credito)
dropdown_conta_credito.grid(row=2, column=1, sticky="w")

label_historico = ttk.Label(janela, text="Histórico:")
label_historico.grid(row=2, column=1, sticky="e")
entry_historico = ttk.Entry(janela)
entry_historico.grid(row=2, column=2, sticky="we", columnspan= 3, padx=10)

# Botões
botao_adicionar = ttk.Button(janela, text="Adicionar Lançamento", command=adicionar_lancamento)
botao_adicionar.grid(row=3, column=0, columnspan=4)

# Treeview - Tabela
tabela = ttk.Treeview(janela, columns=("Data", "Conta Débito", "Conta Crédito", "Valor", "Histórico"), show="headings")

# Set the column widths
tabela.column("Data", width=100)
tabela.column("Conta Débito", width=100)
tabela.column("Conta Crédito", width=100)
tabela.column("Valor", width=100)
tabela.column("Histórico", width=200)

# Set the column headers
tabela.heading("Data", text="Data")
tabela.heading("Conta Débito", text="Conta Débito")
tabela.heading("Conta Crédito", text="Conta Crédito")
tabela.heading("Valor", text="Valor")
tabela.heading("Histórico", text="Histórico")

# Add the table to the window
tabela.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Configure grid weights to make the widgets responsive
janela.grid_rowconfigure(4, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_columnconfigure(3, weight=1)

# Executar a janela principal
janela.mainloop()
