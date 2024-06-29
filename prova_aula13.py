class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros = valor / self.valor_litro
        self.quantidade_combustivel -= litros
        return litros

    def abastecer_por_litro(self, litros):
        valor = litros * self.valor_litro
        self.quantidade_combustivel -= litros
        return valor

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade

bomba = BombaCombustivel("Gasolina", 4.50, 500)

litros = bomba.abastecer_por_valor(100)
print(f"Abastecidos {litros:.2f} litros de {bomba.tipo_combustivel}")

valor = bomba.abastecer_por_litro(20)
print(f"Valor a pagar: R$ {valor:.2f}")

bomba.alterar_valor(4.70)

bomba.alterar_combustivel("Etanol")

bomba.alterar_quantidade_combustivel(300)
