# Quadro Algoritmo — Previsão de Gastos com Regressão Linear

Este projeto faz parte das atividades do curso de Ciência da Computação (2º semestre) e tem como objetivo demonstrar, via Python, o uso de algoritmos de **regressão linear** para prever os gastos mensais, utilizando dados de despesas organizados por categorias e datas.

## Visão Geral

O diretório contém um sistema que:
- Lê dados históricos de despesas (`data/despesas.json` ou `data/dados.py`)
- Processa as despesas, focando principalmente na categoria "Alimentação"
- Treina um modelo de **regressão linear** utilizando Scikit-Learn
- Realiza a previsão do gasto do mês seguinte
- Plota um gráfico com os valores históricos e a previsão usando Matplotlib

## Estrutura dos Arquivos

- `main.py`: Executa o fluxo principal de leitura dos dados, processamento e chamada dos métodos de previsão.
- `regrescao_linar.py`: Contém as funções de manipulação de dados, treinamento do modelo e geração do gráfico.
- `data/dados.py`: Amostra dos dados no formato Python (lista de dicionários de despesas).
- `data/despesas.json`: Mesmo formato dos dados, mas em JSON.
  
## Principais Tecnologias Utilizadas

- **Python 3**
- **Pandas**
- **NumPy**
- **Scikit-Learn** (regressão linear)
- **Matplotlib**

## Como Executar

1. Instale as dependências necessárias:
   ```bash
   pip install pandas numpy scikit-learn matplotlib
   ```

2. Certifique-se de que o arquivo de dados existe em `data/despesas.json` ou `data/dados.py`.

3. Execute o script principal:
   ```bash
   python main.py
   ```

4. O programa irá processar os dados, prever o gasto do próximo mês e exibir um gráfico com os resultados.

## Estrutura Esperada do JSON/Dados

Exemplo de entrada (`despesas.json`):

```json
[
  {"tag": "Alimentação", "valor": 50, "data": "2024-07-01", "prioridade": 2},
  {"tag": "Lazer", "valor": 80, "data": "2024-07-04", "prioridade": 2},
  ...
]
```

## Detalhes Técnicos

- Apenas despesas com tag `"Alimentação"` são efetivamente consideradas para previsão por padrão.
- O gráfico exibe:
  - Valores históricos mensais (linha azul)
  - Previsão para o mês seguinte (linha vermelha tracejada)

## Licença

Didático, código aberto para fins educacionais.
