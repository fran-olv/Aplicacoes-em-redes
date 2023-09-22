class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def exibir_informacoes(self):
        print("Nome da loja:", self.nome)
        print("Endereço da loja:", self.endereco)


class Vendedor:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def exibir_informacoes(self):
        print("Nome do vendedor:", self.nome)
        print("Código do vendedor:", self.codigo)

    def realizar_venda(self, cliente, pizza):
        print("Venda realizada pelo vendedor", self.nome)
        cliente.efetuar_pagamento(pizza)


class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def exibir_informacoes(self):
        print("Nome do cliente:", self.nome)
        print("Endereço do cliente:", self.endereco)

    def efetuar_pagamento(self, pizza):
        print("Pagamento efetuado pelo cliente", self.nome)
        self.receber_pizza(pizza)

    def receber_pizza(self, pizza):
        print("Pizza recebida pelo cliente", self.nome)
        pizza.exibir_detalhes()


class Pizza:
    def __init__(self, sabor, tamanho, preco):
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = preco

    def exibir_detalhes(self):
        print("Detalhes da pizza:")
        print("Sabor:", self.sabor)
        print("Tamanho:", self.tamanho)
        print("Preço:", self.preco)


class Cardapio:
    def __init__(self):
        self.pizzas = []

    def adicionar_pizza(self, pizza):
        self.pizzas.append(pizza)

    def exibir_cardapio(self):
        print("Cardápio:")
        for i, pizza in enumerate(self.pizzas, start=1):
            print(f"{i}. {pizza.sabor} - R${pizza.preco}")
