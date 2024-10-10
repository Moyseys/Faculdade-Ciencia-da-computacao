import calendar
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
from dados import despesas 

# Formatar despesas por tag e mês
despesas_formatada = {}
for despesa in despesas:
    mes = datetime.strptime(despesa['data'], "%Y-%m-%d").month
    valor = despesa['valor']
    tag = despesa['tag']

    if tag == "Lazer":
        despesas_formatada[mes] = valor

# Preparar os dados para o modelo
x = np.array(list(despesas_formatada.keys())).reshape(-1, 1)  
y = np.array(list(despesas_formatada.values()))

# Criar DataFrame
df = pd.DataFrame({
    'mes': x.flatten(),
    'gastos': y
})

# Treinando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(x, y)

# Previsão para os meses existentes
y_pred = modelo.predict(x)

# Identificar o próximo mês com base no último mês disponível
ultimo_mes = max(despesas_formatada.keys())
proximo_mes = ultimo_mes + 1 if ultimo_mes < 12 else 1  # Se o último mês for dezembro, volta para janeiro (1)

# Prever o gasto para o próximo mês
gasto_proximo_mes = modelo.predict(np.array([[proximo_mes]]))

# Adicionar o próximo mês e a previsão ao DataFrame
df = df._append({'mes': proximo_mes, 'gastos': gasto_proximo_mes[0]}, ignore_index=True)

# Atualizar a lista de meses
meses_nome = [calendar.month_name[n_mes] for n_mes in df['mes']]

# Recalcular as previsões para todos os meses incluindo o próximo
x_novo = np.array(df['mes']).reshape(-1, 1)
y_pred_novo = modelo.predict(x_novo)

# Plotar o gráfico com a previsão do próximo mês
plt.figure(figsize=(10, 6))
plt.plot(meses_nome, df['gastos'], marker='o', label='Gastos Mensais')
plt.plot(meses_nome, y_pred_novo, color='red', linestyle='--', label='Previsão de Gastos')
plt.title('Gastos Mensais e Previsão')
plt.xlabel('Meses')
plt.ylabel('Gastos')
plt.legend()
plt.grid()
plt.show()

# Exibir o valor previsto
print(f"Previsão de gasto para o próximo mês ({calendar.month_name[proximo_mes]}): R$ {gasto_proximo_mes[0]:.2f}")
