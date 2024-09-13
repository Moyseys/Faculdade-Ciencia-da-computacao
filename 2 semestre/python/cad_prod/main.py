import sqlite3
from tkinter import *

#Criando janela principal
root = Tk()
root.title("Cadastro de Produtos")

#Conexão com o banco de dados SQlite
conn = sqlite3.connect("produto.db")
c = conn.cursor()

# Criando a tabela se não existir
c.execute('''CREATE TABLE IF NOT EXISTS produto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            qtd INTEGER,
            preco REAL,
            data TEXT
            )
            ''')
#Função para adicionar um novo usuário
def adicionar_produto():
    nome = entry_nome.get()
    qtd = entry_qtd.get()
    preco = entry_preco.get()
    data = entry_data.get()
    
    c.execute("INSERT INTO produto (nome, qtd, preco, data) VALUES (?, ?, ?, ?)", (nome, qtd, preco, data))
    conn.commit()
    entry_nome.delete(0, END)
    entry_qtd.delete(0, END)
    entry_preco.delete(0, END)
    entry_data.delete(0, END)
    ler_produto()
#Função para ler e exibir 
def ler_produto():
    c.execute("SELECT * FROM produto")
    registros = c.fetchall()

    #Limpa a exibição anterior
    for widget in frame_registros.winfo_children():
        widget.destroy()
    
    for registro in registros:
        label = Label(frame_registros, text=f"ID: {registro[0]} | Nome: {registro[1]} | Qtd: {registro[2]} | Preço: {registro[3]} | Data: {registro[4]}")
        label.pack()

#Campos de entrada
Label(root, text= "Nome", width=100).pack(pady=5)
entry_nome = Entry(root)
entry_nome.pack(pady=5)

Label(root, text= "Qtd", width=100).pack(pady=5)
entry_qtd = Entry(root)
entry_qtd.pack(pady=5)

Label(root, text= "Preço", width=100).pack(pady=5)
entry_preco = Entry(root)
entry_preco.pack(pady=5)

Label(root, text= "Data", width=100).pack(pady=5)
entry_data = Entry(root)
entry_data.pack(pady=5)

#Botão adiconar usuario
btn_add = Button(root, text="Adicionar produto", command=adicionar_produto)
btn_add.pack(pady=10)

#Frame para exibir os produto cadastrados
frame_registros = Frame(root)
frame_registros.pack(pady=20, padx=20)

# Exibir os produto ao iniciar
ler_produto()

#Executar a janela
root.mainloop()

# Fechando a conexão com o banco de dados ao fechar
conn.close()