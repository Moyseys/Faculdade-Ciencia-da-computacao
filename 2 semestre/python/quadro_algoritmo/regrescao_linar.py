import calendar
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from data.dados import despesas 
import matplotlib.pyplot as plt

despesas_formatada = {}
qtd_mes = 0
for i, despesa in enumerate(despesas):
    mes = datetime.strptime(despesa['data'], "%Y-%m-%d").month
    valor = despesa['valor']
    tag = despesa['tag']

    if tag == "Alimentação":
        despesas_formatada[mes] = valor

meses_nome = [calendar.month_name[n_mes] for n_mes in despesas_formatada.keys()]
x = np.array(list(despesas_formatada.keys())).reshape(-1, 1)  
y = np.array(list(despesas_formatada.values()))

# Criar DataFrame
df = pd.DataFrame({
    'mes': x.flatten(),
    'gastos': y
})
modelo = LinearRegression()

# Treinando o modelo
# x Variável independente
# y Variavel dependente
modelo.fit(x, y)

# Identificar o próximo mês com base no último mês disponível
ultimo_mes = max(despesas_formatada.keys())
proximo_mes = ultimo_mes + 1 if ultimo_mes < 12 else 1

# Prever o gasto para o próximo mês
gasto_proximo_mes = modelo.predict(np.array([[proximo_mes]]))
df = df._append({'mes': proximo_mes, 'gastos': gasto_proximo_mes[0]}, ignore_index=True)
# Atualizar a lista de meses
meses_nome = []
for m in df['mes']:
    meses_nome.append(calendar.month_name[int(m)])

# Recalcular as previsões para todos os meses incluindo o próximo   
x_novo = np.array(df['mes']).reshape(-1, 1)
y_pred = modelo.predict(x_novo)

plt.figure(figsize=(10, 6))
plt.plot(meses_nome, df['gastos'], marker='o', label='Gastos Mensais')
plt.plot(meses_nome, y_pred, color='red', linestyle='--', label='Previsão de Gastos')
plt.title('Gastos Mensais e Previsão')
plt.xlabel('Meses')
plt.ylabel('Gastos')
plt.legend()
plt.grid()
plt.show()