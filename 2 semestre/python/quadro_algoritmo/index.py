import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def calcular_total_despesas(despesas):
    total = sum(despesa["valor"] for despesa in despesas)
    return total

def calcular_despesas_por_tag(despesas):
    res = {
        "Alimentação": 0,
        "Lazer": 0,
        "Saúde": 0,
        "Carro": 0,
    }
    for despesa in despesas:
        tag = despesa["tag"]
        valor = despesa["valor"]
        res[tag] += valor
    return res

def calcular_media_por_prioridade(despesas, prioridades):
    total_despesas = calcular_total_despesas(despesas)
    soma_prioridades = sum(prioridades.values())
    valor_por_prioridade = total_despesas / soma_prioridades
    media_por_prioridade = {tag: valor_por_prioridade * prio_valor for tag, prio_valor in prioridades.items()}
    return media_por_prioridade

def sugerir_remanejamento(media_por_prioridade, total_por_tag):
    for tag, valor in media_por_prioridade.items():
        ideal_por_tag = valor
        valor_por_tag = total_por_tag[tag]

        redundancia = 0.95
        margem_de_redundancia = ideal_por_tag / redundancia

        if valor_por_tag > margem_de_redundancia:
            print(f"Sugestão de remanejamento: remover {valor_por_tag - margem_de_redundancia} à tag {tag}")



despesas = [
    {"tag": "Alimentação", "valor": 50},
    {"tag": "Alimentação", "valor": 30},
    {"tag": "Alimentação", "valor": 100},
    {"tag": "Lazer", "valor": 80},
    {"tag": "Lazer", "valor": 20},
    {"tag": "Lazer", "valor": 200},
    {"tag": "Saúde", "valor": 60},
    {"tag": "Carro", "valor": 40}
]

prioridades = {
    "Alimentação": 4,
    "Saúde": 3,
    "Carro": 2,
    "Lazer": 1,
}

total = calcular_total_despesas(despesas)
print(f"{Fore.CYAN}Total de despesas: {Style.BRIGHT}{total}")

total_por_tag = calcular_despesas_por_tag(despesas)
print(f"{Fore.MAGENTA}Total de despesas por tag: {Style.BRIGHT}{total_por_tag}")

media_por_prioridade = calcular_media_por_prioridade(despesas, prioridades)
print(f"{Fore.GREEN}A média de cada prioridade é: {Style.BRIGHT}{media_por_prioridade}")


sugerir_remanejamento(media_por_prioridade, total_por_tag)