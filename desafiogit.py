print("Análise de Vendas")
produtos = [
    {"nome": "produto A", "valor_unit": 5.50, "quantidade": 10},
    {"nome": "produto B", "valor_unit": 6.90, "quantidade": 32},
    {"nome": "produto C", "valor_unit": 8.69, "quantidade": 14},
]
def calcular_total_quantidade(produtos):
    total_quantidade = sum(produto["quantidade"] for produto in produtos)
    return total_quantidade

def media_quantidade(produtos):
    media_total = sum(produto["quantidade"] for produto in produtos) / 3
    return media_total

def calcular_valor_total_vendido(produtos):
    for produto in produtos:
        valor_total = produto["valor_unit"] * produto["quantidade"]
        print(f"Valor total vendido de {produto['nome']}: R$ {valor_total:.2f}")

    
resultado = calcular_total_quantidade(produtos)
media = media_quantidade(produtos)
vlr_total = calcular_valor_total_vendido(produtos)

print(resultado)
print(f"{media:.2f}")
print("f{vlr_total:.2f}")
