from colorama import Fore, Style, init
init(autoreset=True)

def exibir_dados(titulo, dados, cor=Fore.WHITE, negrito=False):
    estilo = Style.BRIGHT if negrito else Style.NORMAL
    print(f"{estilo}{cor}{titulo}:")
    print(f"{estilo}{cor}-" * 30)

    for tag, valor in dados.items():
        print(f"{estilo}{cor}{tag:<15}: R$ {valor:.2f}") 

    print(f"{estilo}{cor}-" * 30)
    total = sum(dados.values())
    print(f"{estilo}{cor}{'Total':<15}: R$ {total:.2f}\n")  