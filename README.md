```markdown
# 🚀 Desafios de Programação em Python

Bem-vindo ao repositório de desafios de programação em Python! Aqui você encontrará soluções para uma série de problemas interessantes, cada um abordando um conceito específico de programação. Vamos explorar juntos! 🌟

## 📋 Índice

1. [Valor da variável SOMA](#1-valor-da-variável-soma)
2. [Sequência de Fibonacci](#2-sequência-de-fibonacci)
3. [Faturamento Diário](#3-faturamento-diário)
4. [Percentual de Faturamento por Estado](#4-percentual-de-faturamento-por-estado)
5. [Inverter String](#5-inverter-string)

## 1. Valor da variável SOMA

### Descrição

O código incrementa `K` de 1 até 13 e soma esses valores em `SOMA`. O valor final de `SOMA` será a soma dos números de 1 a 13, que é 91.

### Código

```python
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(SOMA)
```


## 2. Sequência de Fibonacci

### Descrição

A função `is_fibonacci` verifica se um número pertence à sequência de Fibonacci. O usuário informa um número e o programa verifica se ele pertence à sequência.

### Código

```python
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

numero = int(input("Informe um número: "))
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
```


## 3. Faturamento Diário

### Descrição

O programa lê os dados de faturamento em formato JSON, calcula o menor e maior valor de faturamento, a média mensal e o número de dias com faturamento acima da média.

### Código

```python
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
```



### Descrição

O programa calcula o percentual de representação de cada estado no faturamento total da distribuidora.

### Código

```python
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")
```


### Descrição

A função `inverter_string` inverte os caracteres de uma string sem usar funções prontas como `reverse`.

### Código

```python
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string)}")
```


---

## 👨‍💻 Autor

Desenvolvido por [Félix David](https://github.com/felixdavidwebdev).

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---


