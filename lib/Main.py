import tkinter as tk
from tkcalendar import DateEntry
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from Db import create_connection_FDB, obter_cod_plano_de_contas

class LancamentoContabil:
    def __init__(self, data, conta_debito, conta_credito, valor, historico):
        self.data = data
        self.conta_debito = conta_debito
        self.conta_credito = conta_credito
        self.valor = valor
        self.historico = historico

def atualizarTabela():
    connection, cursor = create_connection_FDB()
    tabela.delete(*tabela.get_children())  # Limpa os dados antigos da tabela

    cursor.execute("select c.data, l.cod_conta_debito, l.cod_conta_credito, l.valor, c.historico from livro_diario l inner join lancamentos_contabeis c on l.cod_lancamento_contabil = c.cod_lancamento")

    resultados = cursor.fetchall()

    for resultado in resultados:
        tabela.insert("", "end", values=resultado)

    connection.commit()  # Confirma as alterações no banco de dados
    connection.close()

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
    numero_conta_credito = conta_credito.split('-')[0].strip()
    conta_credito = int(numero_conta_credito)  
    numero_conta_debito = conta_debito.split('-')[0].strip()  # Extrai o número antes do hífen
    conta_debito = int(numero_conta_debito) 

    valor = float(entry_valor.get())
    historico = entry_historico.get()
    data = entry_data.get_date()
    connection, cursor = create_connection_FDB()
    cursor.execute("insert into livro_diario (valor, cod_conta_credito, cod_conta_debito) values (%s, %d, %d)" % (valor, int(conta_credito), int(conta_debito)))
    connection.commit()
    cursor.execute("insert into lancamentos_contabeis (historico,data) values (%s, %s, %s)" % (historico, data))
    connection.commit()  # Confirma as alterações no banco de dados
    connection.close()
    atualizarTabela()
    

# Criação do livro diário
livro_diario = LivroDiario()

# Criação da janela principal
janela = ThemedTk(theme="equilux", themebg=True)
janela.iconbitmap('lib\icon\icon.ico')
janela.title("Livro Diário")
janela.minsize(750, 350)

# Labels
label_data = ttk.Label(janela, text="Data:")
label_data.grid(row=1, column=1, sticky="e")
entry_data = DateEntry(janela, date_pattern="dd/mm/yyyy", width=12, background='darkblue', foreground='white',
                       borderwidth=2)
entry_data.grid(row=1, column=2, sticky="w")

cursor, connection = create_connection_FDB()
contas_debito = obter_cod_plano_de_contas(connection,cursor)
cursor, connection = create_connection_FDB()
contas_credito = obter_cod_plano_de_contas(connection,cursor)
connection.close()

label_conta_debito = ttk.Label(janela, text="Conta Débito:")
label_conta_debito.grid(row=1, column=0, sticky="e")
var_conta_debito = tk.StringVar()
combobox_conta_debito = ttk.Combobox(janela, textvariable=var_conta_debito, values=contas_debito, state="readonly")
combobox_conta_debito.grid(row=1, column=1, sticky="w")

label_valor = ttk.Label(janela, text="Valor:")
label_valor.grid(row=1, column=2, sticky="e")
entry_valor = ttk.Entry(janela)
entry_valor.grid(row=1, column=3, sticky="we", padx=10)

label_conta_credito = ttk.Label(janela, text="Conta Crédito:")
label_conta_credito.grid(row=2, column=0, sticky="e")
var_conta_credito = tk.StringVar()
combobox_conta_credito = ttk.Combobox(janela, textvariable=var_conta_credito, values=contas_credito, state="readonly")
combobox_conta_credito.grid(row=2, column=1, sticky="w")

label_historico = ttk.Label(janela, text="Histórico:")
label_historico.grid(row=2, column=1, sticky="e")
entry_historico = ttk.Entry(janela)
entry_historico.grid(row=2, column=2, sticky="we", columnspan= 3, padx=10)

# Botões
botao_adicionar = ttk.Button(janela, text="Adicionar Lançamento", command=adicionar_lancamento)
botao_adicionar.grid(row=3, column=0, columnspan=4)


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Adicionar botões de baixo
botao_atualizar = ttk.Button(janela, text="Atualizar", command=atualizarTabela)
botao_atualizar.grid(row=5, column=0, padx=10, pady=10)

botao_2 = ttk.Button(janela, text="Botão 2", command=lambda: print("2"))
botao_2.grid(row=5, column=1)

botao_3 = ttk.Button(janela, text="Botão 3", command=lambda: print("3"))
botao_3.grid(row=5, column=2)

botao_4 = ttk.Button(janela, text="Botão 4", command=lambda: print("4"))
botao_4.grid(row=5, column=3)

#alguma merda do cleiton
style = ttk.Style()
style.configure('TCombobox', postoffset=(0, 0, 100, 0))

# Configure grid weights to make the widgets responsive
janela.grid_rowconfigure(4, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_columnconfigure(3, weight=1)

# Executar a janela principal
janela.mainloop()
