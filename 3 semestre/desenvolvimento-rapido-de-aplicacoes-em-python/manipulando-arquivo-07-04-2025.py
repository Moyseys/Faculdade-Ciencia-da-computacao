fileName = "arquivo"

# Crie um programa com o seguinte menu:

# 1. Criar um arquivo
# 2. Acrescentar linhas ao arquivo
# 3. Mostrar o conteudo do arquivo
# 0. Sair

def showMenu():
    print("""
        1. Criar um arquivo
        2. Acrescentar linhas ao arquivo
        3. Mostrar o conteudo do arquivo
        0. Sair
    """)
    opt = input("Selecione uma opção: ")
    return opt


optSelected = showMenu()

# Onde na opcao 1, o usuario pode informar um nome de arquivo.
# Caso não seja informado, considere 'arquivo.txt' como nome inicial
# para as demais funcionalidades do programa.

# Opcao: 1
# Informe o nome do arquivo: [arquivo.txt]

if(optSelected == "1"):
    fileName = input("Insira o nome do arquivo: ")
    if(not fileName):
        fileName = "arquivo"

    open(fileName+"txt", "w")

# A opcao de insercao de dados deve permitir o acrescimo de quantas
# linhas o usuario desejar ate' encontrar uma condicao de parada, 
# como somente o numero zero, por exemplo.

# Opcao: 2
# > Segunda linha
# > TERCEIRA LINHA
# > QuArTa linha
# > 0

# Apos o recebimento de cada linha, tratar a informacao para que o
# texto armazenado seja uma linha com todo o conteudo em caixa baixa
# tendo apenas a letra inicial da frase em maiusculo

if(optSelected == "2"):
    f = open(fileName+"txt", "w")
    while(True):
        linha = input("Linha: ")
        if (linha == "0"):
            f.close()
            break 
        linha = linha.lower()
        f.write(linha+"\n")

# A opcao de leitura mostrara' o conteudo do arquivo

# Opcao: 3
# Esta eh a primeira linhas

if(optSelected == "3"):
    f = open(fileName+'txt', 'r')
    for line in f:
        print(line)

# Opcao: _
