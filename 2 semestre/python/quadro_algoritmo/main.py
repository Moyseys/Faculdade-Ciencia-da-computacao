import json
import os
from regrescao_linar import adiciona_previsao_proximo_mes, calcula_previsao, formata_despesas, gera_meses_nome, plota_grafico, prepara_dados, treina_modelo

file_json_data = os.path.relpath("data/despesas.json")
with open(file_json_data, 'r') as file:
    data = json.load(file)

despesas_formatada = formata_despesas(data)
df, x, y = prepara_dados(despesas_formatada)
modelo = treina_modelo(x, y)
df = adiciona_previsao_proximo_mes(df, modelo)
meses_nome = gera_meses_nome(df)
y_pred = calcula_previsao(modelo, df)
plota_grafico(df, y_pred, meses_nome)