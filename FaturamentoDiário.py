import json

# Exemplo de dados em JSON
dados = '''
[
    {"dia": 1, "valor": 1000.0},
    {"dia": 2, "valor": 1500.0},
    {"dia": 3, "valor": 0.0},
    {"dia": 4, "valor": 2000.0},
    {"dia": 5, "valor": 0.0}
]
'''

faturamento = json.loads(dados)

valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Dias acima da média: {dias_acima_da_media}")
