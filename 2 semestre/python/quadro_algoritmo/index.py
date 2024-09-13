tags = [
    {
        "tag": "Alimentação",
        "valor": 50
    },
    {
        "tag": "Alimentação",
        "valor": 30
    },
    {
        "tag": "Alimentação",
        "valor": 100
    },
    {
        "tag": "Lazer",
        "valor": 80
    },
    {
        "tag": "Lazer",
        "valor": 20
    },
    {
        "tag": "Lazer",
        "valor": 200
    },
    {
        "tag": "Saúde",
        "valor": 60
    },
    {
        "tag": "Carro",
        "valor": 40
    }
]

res = {
    "Alimentação": 0,
    "Lazer": 0,
    "Saúde": 0,
    "Carro": 0,
}
for tag in tags:
    currentTag = tag["tag"]
    currentValue = tag["valor"] 
    res[currentTag] = currentValue + res[currentTag]

print(res)