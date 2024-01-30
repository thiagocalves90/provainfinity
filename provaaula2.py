#Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado
#e o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h

velocidade = int(input("Informe a velocidade do carro: "))
multa = (velocidade - 80) * 20

if velocidade <= 80:
    print("A velocidade está dentro do permitido da via.")
else:
    print(f"Você foi multado e a multa foi de: R$ {multa} ")