# Criação do dicionário "estoque" com informações sobre produtos
estoque = {
   'Produto1': (19.99, 50),
   'Produto2': (9.99, 30),
   'Produto3': (12.49, 25),
   'Produto4': (6.99, 40),
   'Produto5': (24.99, 20)
}

# Função para calcular o valor total do estoque
def total_valor_estoque(estoque):
   total = 0
   for produto, (preco, quantidade) in estoque.items():
       valor_produto = preco * quantidade
       total += valor_produto
   return total

# Chamada da função para calcular o valor total do estoque
valor_total = total_valor_estoque(estoque)
print(f'O valor total do estoque é: R${valor_total:.2f}')