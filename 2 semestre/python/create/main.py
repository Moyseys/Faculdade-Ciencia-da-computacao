import sqlite3
from tkinter import *

#Criando janela principal
root = Tk()
root.title("Cadastro de Usuários")

#Conexão com o banco de dados SQlite
conn = sqlite3.connect("usuarios.db")
c = conn.cursor()

# Criando a tabela se não existir
c.execute('''CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
            )
            ''')
#Função para adicionar um novo usuário
def adicionar_usuario():
    nome = entry_nome.get()
    idade = entry_idade.get()
    
    c.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
    conn.commit()
    entry_nome.delete(0, END)
    entry_idade.delete(0, END)
    ler_usuarios()
#Função para ler e exibir 
def ler_usuarios():
    c.execute("SELECT * FROM usuarios")
    registros = c.fetchall()

    #Limpa a exibição anterior
    for widget in frame_registros.winfo_children():
        widget.desfroy()
    
    for registro in registros:
        label = Label(frame_registros, text=f"ID: {registro[0]} | Nome: {registro[1]} | Idade: {registro[2]}")
        label.pack()

#Campos de entrada
Label(root, text= "Nome", width=100).pack(pady=5)
entry_nome = Entry(root)
entry_nome.pack(pady=5)

Label(root, text= "Idade", width=100).pack(pady=5)
entry_idade = Entry(root)
entry_idade.pack(pady=5)

#Botão adiconar usuario
btn_add = Button(root, text="Adicionar usuário", command=adicionar_usuario)
btn_add.pack(pady=10)

#Frame para exibir os usuarios cadastrados
frame_registros = Frame(root)
frame_registros.pack(pady=20, padx=20)

# Exibir os usuarios ao iniciar
ler_usuarios()

#Executar a janela
root.mainloop()

# Fechando a conexão com o banco de dados ao fechar
conn.close()