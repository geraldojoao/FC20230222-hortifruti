class Caixa:
    def __init__(self):
        self.valor_inicial = 0.0
        self.vendas = []

    def abrir_caixa(self, valor_inicial):
        self.valor_inicial = valor_inicial
        print(f"O caixa está iniciando com R$ {self.valor_inicial:.2f}")

    def fechar_caixa(self):
        total_vendas = sum(venda.total for venda in self.vendas)
        lucro = total_vendas + self.valor_inicial
        print(f"Caixa finalizado. Total de vendas: R$ {total_vendas:.2f}, Lucro: R$ {lucro:.2f}")

    def registrar_venda(self, venda):
        self.vendas.append(venda)
