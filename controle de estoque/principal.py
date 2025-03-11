from classes import Produto, Estoque

produto1 = Produto('Camiseta', 29.90, 50)
produto2 = Produto("Calça Jeans", 99.90, 30)
produto3 = Produto("Tênis", 150.00, 10)
produto4 = Produto('Bermuda', 30.00, 50)

estoque = Estoque()
estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)
estoque.adicionar_produto(produto3)
estoque.adicionar_produto(produto4)


print('\nProdutos no estoque:')
estoque.listar_produtos()

estoque.remover_produto('Camiseta')
estoque.remover_produto('Bermuda')


print("\nProdutos no estoque após remoção:")
estoque.listar_produtos()