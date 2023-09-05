'''
    Crie um dicionário chamado "estoque" com informações sobre alguns produtos:
    - Chave: Nome do produto
    - Valor: Tupla contendo preço e quantidade em estoque
    Adicione pelo menos 5 produtos ao dicionário.
    Crie uma função chamada "total_valor_estoque" que calcula o valor total do estoque (preço
    * quantidade) para todos os produtos no dicionário.
'''

estoque = {
    "Esmalte": (2.50, 100),
    "L'oreal Paris Shampoo": (250, 30),
    "L'oreal Paris Condicionador": (260, 50),
    "Wella Nutritive Kit": (299.99, 20),
    "Kit manicure iniciante": (35, 15)
}

def total_valor_estoque(estoque):
    for preco, quantidade in estoque.items():
        valorProduto = preco * quantidade
        totalEstoque += valorProduto
    return totalEstoque

print(total_valor_estoque(estoque))