print("Análise de Vendas")

produtos = [
    {"Nome": "Produto A", "Valor Unit": 5.50, "Quantidade": 10},
    {"Nome": "Produto B", "Valor Unit": 6.90, "Quantidade": 32},
    {"Nome": "Produto C", "Valor Unit": 8.69, "Quantidade": 14},
]

# Inicializa as variáveis para armazenar os produtos com maior e menor valor total
produto_mais_vendido = None
produto_menos_vendido = None
valor_maximo = -float('inf')
valor_minimo = float('inf')

# Itera sobre a lista de produtos para calcular o valor total e identificar o maior e o menor
for produto in produtos:
    valor_total = produto["Valor Unit"] * produto["Quantidade"]
    
    if valor_total > valor_maximo:
        valor_maximo = valor_total
        produto_mais_vendido = produto
    
    if valor_total < valor_minimo:
        valor_minimo = valor_total
        produto_menos_vendido = produto

# Exibe o produto com o maior valor total de vendas
print(f"Produto com o maior valor total de vendas:")
print(f"Nome: {produto_mais_vendido['Nome']}")
print(f"Valor Unit: {produto_mais_vendido['Valor Unit']}")
print(f"Quantidade: {produto_mais_vendido['Quantidade']}")
print(f"Valor Total: {produto_mais_vendido['Valor Unit'] * produto_mais_vendido['Quantidade']:.2f}")

# Exibe o produto com o menor valor total de vendas
print(f"\nProduto com o menor valor total de vendas:")
print(f"Nome: {produto_menos_vendido['Nome']}")
print(f"Valor Unit: {produto_menos_vendido['Valor Unit']}")
print(f"Quantidade: {produto_menos_vendido['Quantidade']}")
print(f"Valor Total: {produto_menos_vendido['Valor Unit'] * produto_menos_vendido['Quantidade']:.2f}")
