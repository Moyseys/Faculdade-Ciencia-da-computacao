import colorama
from colorama import Fore, Style

from utils.exibicao import exibir_dados

colorama.init(autoreset=True)

def calcular_total_despesas(despesas):
    total = sum(despesa["valor"] for despesa in despesas)
    return total

def calcular_despesas_por_tag(despesas):
    res = {}
    for despesa in despesas:
        tag = despesa["tag"]
        if tag not in res:
            res[tag] = 0
        
        valor = despesa["valor"]
        res[tag] += valor
    return res

def calcular_limite_por_tag(despesas, prioridades):
    total_despesas = calcular_total_despesas(despesas)
    soma_prioridades = sum(prioridades.values())
    valor_por_prioridade = total_despesas / soma_prioridades
    limite_por_tag = {}

    for tag, prio_valor in prioridades.items():
        limite_por_tag[tag] = valor_por_prioridade * prio_valor

    return limite_por_tag

def sugerir_remanejamento(limite_por_tag, total_por_tag):
    sugestoes = []
    for tag, valor in limite_por_tag.items():
        limite_atual = valor
        valor_atual = total_por_tag[tag]

        margem_de_redundancia_limite = limite_atual + (limite_atual * 0.05)
        margem_de_redundancia_aviso = limite_atual - (limite_atual * 0.20)

        #Caso tenha passado do limite da tag atual faz uma sugestão de remover investimento em tau 
        if valor_atual >= margem_de_redundancia_limite:
            sugestoes.append(f"{Fore.RED}Atenção: Você ultrapassou o limite de {margem_de_redundancia_limite} para a tag '{tag}'. É recomendado remover {valor_atual - margem_de_redundancia_limite:.2f} do seu investimento.{Style.RESET_ALL}")
        elif valor_atual < margem_de_redundancia_limite and valor_atual >= margem_de_redundancia_aviso:
            sugestoes.append(f"{Fore.YELLOW}Alerta: Você está se aproximando do limite recomendado de {margem_de_redundancia_limite} para a tag '{tag}'.{Style.RESET_ALL}")

    return sugestoes


despesas = [
    {"tag": "Alimentação", "valor": 50},
    {"tag": "Alimentação", "valor": 30},
    {"tag": "Alimentação", "valor": 100},
    {"tag": "Lazer", "valor": 80},
    {"tag": "Lazer", "valor": 20},
    {"tag": "Lazer", "valor": 200},
    {"tag": "Saúde", "valor": 60},
    {"tag": "Carro", "valor": 40},
    {"tag": "Carro", "valor": 100}
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
exibir_dados("Resumo de despesas", total_por_tag, Fore.MAGENTA, True)

limite_por_tag = calcular_limite_por_tag(despesas, prioridades)
exibir_dados("A média de cada prioridade", limite_por_tag, Fore.GREEN, True)


sugestoes = sugerir_remanejamento(limite_por_tag, total_por_tag)
for s in sugestoes:
    print(s)