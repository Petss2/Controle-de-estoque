class Produto():
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade


    def __str__(self):
        return f'Produto: {self.nome}, Preço: {self.preço}, Quantidade: {self.quantidade}'
    

class Estoque():
    def __init__(self):
        self.produtos = []
    

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f'{produto.nome} foi adicionado ao estoque.')


    def remover_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                self.produtos.remove(produto)
                print(f'{produto.nome} foi removido do estoque.')
                return
        print(f'Produto {nome_produto} não encontrado no estoque.')

    
    def listar_produtos(self):
        if not self.produtos:
            print('Não há produtos no estoque')
        else:
            for produto in self.produtos:
                print(produto)

    
        
        