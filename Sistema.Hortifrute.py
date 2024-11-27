from Caixa import Caixa
from Produto import Produto
from Venda import Venda


class Lista:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto, quantidade):
        for p in self.produtos:
            if p.codigo == produto.codigo:
                p.quantidade += quantidade
                print(f"Quantidade de {produto.nome} atualizada. Novo estoque: {p.quantidade}.")
                return
        produto.quantidade = quantidade
        self.produtos.append(produto)
        print(f"Produto {produto.nome} adicionado com sucesso ao estoque.")

    def remover_produto(self, codigo, quantidade):
        produto = self.buscar_produto(codigo)
        if produto:
            if produto.quantidade >= quantidade:
                produto.quantidade -= quantidade
                print(f"{quantidade} unidade(s) do produto {produto.nome} removida(s).")
                if produto.quantidade == 0:
                    self.produtos.remove(produto)
                    print(f"Produto {produto.nome} removido completamente do estoque.")
            else:
                print(f"Estoque insuficiente para remover {quantidade} unidade(s) do produto {produto.nome}.")
        else:
            print("Produto não encontrado.")

    def buscar_produto(self, codigo):
        return next((produto for produto in self.produtos if produto.codigo == codigo), None)

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto no estoque.")
            return
        print("Produtos em estoque:")
        for produto in self.produtos:
            print(f"{produto.nome} (Código: {produto.codigo}) - Quantidade: {produto.quantidade}")

class SistemaSupermercado:
    def __init__(self):
        self.lista_produtos = Lista()
        self.caixa = Caixa()

    def cadastrar_produto(self, codigo, nome, valor, tipo, quantidade, validade=None, garantia=None):
        if tipo == "legume" or tipo == "verdura":
            produto = Produto(codigo, nome, valor, validade)
        elif tipo == "fruta":
            produto = Produto(codigo, nome, valor, garantia=garantia)
        else:
            print("Tipo de produto inválido.")
            return
        self.lista_produtos.adicionar_produto(produto, quantidade)

    def iniciar_venda(self):
        venda = Venda()
        while True:
            print("\nMenu de Vendas:")
            print("1. Adicionar produto")
            print("2. Remover produto")
            print("3. Finalizar venda")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                codigo = input("Digite o código do produto: ")
                produto = self.lista_produtos.buscar_produto(codigo)
                if produto:
                    quantidade = int(input("Digite a quantidade: "))
                    venda.adicionar_produto(produto, quantidade)
                    print(f"Produto {produto.nome} adicionado. Total da venda: R$ {venda.total:.2f}")
                else:
                    print("Produto não encontrado.")
            elif opcao == "2":
                codigo = input("Digite o código do produto a remover: ")
                produto = self.lista_produtos.buscar_produto(codigo)
                if produto:
                    print(f"Quantidade em estoque de {produto.nome}: {produto.quantidade} unidade(s).")
                    quantidade = int(input("Digite a quantidade a ser removida: "))
                    self.lista_produtos.remover_produto(codigo, quantidade)
                    print(f"Total da venda: R$ {venda.total:.2f}")
                else:
                    print("Produto não encontrado.")
            elif opcao == "3":
                itens_venda, total_venda = venda.finalizar_venda()
                print("Itens vendidos:")
                for item, quantidade in itens_venda:
                    print(f"{item.nome} - {quantidade} un = R$ {item.valor * quantidade:.2f}")
                self.caixa.registrar_venda(venda)
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_principal(self):
        while True:
            print("\nMenu Principal:")
            print("1. Cadastrar Produto")
            print("2. Buscar Produto")
            print("3. Remover Produto")
            print("4. Iniciar Venda")
            print("5. Abrir Caixa")
            print("6. Fechar Caixa")
            print("7. Listar Produtos em Estoque")
            print("8. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_produto_cli()
            elif opcao == "2":
                self.buscar_produto_cli()
            elif opcao == "3":
                self.remover_produto_cli()
            elif opcao == "4":
                self.iniciar_venda()
            elif opcao == "5":
                valor_inicial = float(input("Digite o valor inicial do caixa: "))
                self.caixa.abrir_caixa(valor_inicial)
            elif opcao == "6":
                self.caixa.fechar_caixa()
            elif opcao == "7":
                self.lista_produtos.listar_produtos()
            elif opcao == "8":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def cadastrar_produto_cli(self):
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        valor = float(input("Digite o valor do produto: "))
        tipo = input("Digite o tipo do produto (legume, verdura, fruta): ")
        quantidade = int(input("Digite a quantidade do produto em estoque: "))
        
        validade = None
        garantia = None

        if tipo == "legume" or tipo == "verdura":
            validade = int(input("Digite a validade do produto (em dias): "))
        elif tipo == "fruta":
            garantia = int(input("Digite a garantia do produto (em meses): "))

        self.cadastrar_produto(codigo, nome, valor, tipo, quantidade, validade, garantia)

    def buscar_produto_cli(self):
        codigo = input("Digite o código do produto que deseja buscar: ")
        produto = self.lista_produtos.buscar_produto(codigo)
        if produto:
            print(f"Produto encontrado: {produto.nome}, Valor: R$ {produto.valor:.2f}, Estoque: {produto.quantidade}")
        else:
            print("Produto não encontrado.")

    def remover_produto_cli(self):
        codigo = input("Digite o código do produto que deseja remover: ")
        produto = self.lista_produtos.buscar_produto(codigo)
        if produto:
            print(f"Quantidade em estoque de {produto.nome}: {produto.quantidade} unidade(s).")
            quantidade = int(input("Digite a quantidade a ser removida: "))
            self.lista_produtos.remover_produto(codigo, quantidade)


if __name__ == "__main__":
    sistema = SistemaSupermercado()
    sistema.menu_principal()
