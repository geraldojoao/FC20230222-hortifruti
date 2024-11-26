class Produto:
    def __init__(self, codigo, nome, valor, validade=None, garantia=None):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.validade = validade  
        self.garantia = garantia  
