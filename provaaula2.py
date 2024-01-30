velocidade = int(input("Informe a velocidade do carro: "))
multa = (velocidade - 80) * 20

if velocidade <= 80:
    print("A velocidade está dentro do permitido da via.")
else:
    print(f"Você foi multado e a multa foi de: R$ {multa} ")
