# HORTIFRUTI PYTHON

**ALUNO:** João Geraldo da Silva Neto, **MATRICULA**:FC20230222

Este é um sistema básico de supermercado desenvolvido em Python. Ele gerencia o estoque de produtos, permite adicionar itens ao carrinho de compras, calcula o valor total da compra e realiza a finalização do processo de compra. 

- **Cadastrar produtos**: Adicionar produtos ao estoque com detalhes como código, nome, preço e data de validade ou garantia.
- **Gerenciar o estoque**: Adicionar e remover produtos do estoque, controlar quantidades e atualizar informações dos produtos.
- **Processar vendas**: Adicionar produtos a uma venda, remover itens, calcular totais e finalizar vendas.
- **Gestão de caixa**: Abrir e fechar o caixa, registrar as vendas totais e calcular o lucro.

## Funcionalidades

- **Cadastro de Produtos**: Cadastrar produtos, incluindo código, nome, preço e atributos opcionais como validade ou garantia.
- **Gerenciamento de Estoque**: Adicionar/remover produtos do estoque, com a capacidade de atualizar quantidades ou remover totalmente itens que esgotaram.
- **Transações de Venda**: Adicionar e remover produtos de uma venda, calcular o preço total e finalizar a venda.
- **Caixa Registradora**: Controlar e fechar o caixa, registrando as vendas totais e calculando o lucro.

## Classes e Suas Funcionalidades

### `Produto`
Representa um produto no supermercado, com os seguintes atributos:

- `codigo`: Identificador único do produto.
- `nome`: Nome do produto.
- `valor`: Preço do produto.
- `validade`: Data de validade para produtos perecíveis (opcional).
- `garantia`: Garantia para produtos que aplicam (opcional).

**Exemplo de uso**:
```python
produto = Produto(codigo="001", nome="Cenoura", valor=3.50, validade=7)
Lista
Gerencia o estoque de produtos, onde é possível adicionar, remover e listar os produtos. Ela também controla as quantidades de cada produto.

Exemplo de uso:

python
Copiar código
lista = Lista()
lista.adicionar_produto(produto, quantidade=10)
Venda
Gerencia as transações de venda, permitindo adicionar e remover produtos, calcular o total e finalizar a venda.

adicionar_produto: Adiciona um produto e sua quantidade à venda.
remover_produto: Remove um produto da venda.
finalizar_venda: Finaliza a venda e retorna os itens vendidos e o valor total.
Exemplo de uso:

python
Copiar código
venda = Venda()
venda.adicionar_produto(produto, 3)  # Adiciona 3 unidades de Cenoura
venda.finalizar_venda()  # Retorna a lista de itens e o total
Caixa
Controla a abertura e o fechamento do caixa, registrando as vendas e calculando o lucro.

Exemplo de uso:

python
Copiar código
caixa = Caixa()
caixa.abrir_caixa(100.0)  # Abre o caixa com um valor inicial
caixa.fechar_caixa()  # Fecha o caixa e mostra as vendas totais e o lucro
SistemaSupermercado
Esta é a classe principal do sistema que integra todas as funcionalidades. Ela permite interagir com o estoque, processar vendas e gerenciar o caixa por meio de um menu simples baseado em texto.

Exemplo de uso:

python
Copiar código
sistema = SistemaSupermercado()
sistema.menu_principal()  # Inicia o menu principal e permite a interação
Instalação
Para rodar este sistema localmente, você precisa ter o Python instalado em sua máquina. Você pode baixar o Python aqui.

Clone o repositório:

bash
Copiar código
git clone https://github.com/seuusuario/sistema-gestao-supermercado.git
Navegue até o diretório do projeto:

bash
Copiar código
cd sistema-gestao-supermercado
Execute o sistema:

bash
Copiar código
python3 sistema_supermercado.py
Como Usar
Ao rodar o sistema, você será apresentado a um menu baseado em texto. O sistema permite que você:

Cadastrar Produto: Adicionar um novo produto ao estoque com detalhes como código, nome, preço, tipo (legume, fruta, etc.), quantidade, validade ou garantia.
Buscar Produto: Buscar um produto pelo código.
Remover Produto: Remover um produto do estoque.
Iniciar Venda: Iniciar uma nova venda, onde você pode adicionar e remover produtos.
Abrir Caixa: Abrir o caixa com um valor inicial.
Fechar Caixa: Fechar o caixa e visualizar as vendas totais e o lucro.
Listar Produtos: Visualizar todos os produtos em estoque com suas quantidades.
Exemplo de Uso do Sistema
python
Copiar código
# Cadastrar um produto
codigo = "001"
nome = "Cenoura"
valor = 3.50
tipo = "legume"
quantidade = 10
validade = 7  # Validade em dias

# Cadastrar o produto no sistema
sistema.cadastrar_produto(codigo, nome, valor, tipo, quantidade, validade)

# Iniciar uma venda
sistema.iniciar_venda()
