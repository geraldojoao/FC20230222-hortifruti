class Venda:
    def __init__(self):
        self.itens = []  # Lista de produtos na venda
        self.total = 0.0

    def adicionar_produto(self, produto, quantidade):
        self.itens.append((produto, quantidade))
        self.total += produto.valor * quantidade

    def remover_produto(self, codigo):
        for item in self.itens:
            if item[0].codigo == codigo:
                self.total -= item[0].valor * item[1]
                self.itens.remove(item)
                break

    def finalizar_venda(self):
        return self.itens, self.total
