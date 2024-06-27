notas = []

while True:
    nota = input("Informe uma nota ou digite '0' para finalizar: ")
    if nota == '0':
        break
    else:
        notas.append(float(nota))

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_situacao(media):
    if media < 7:
        return "Reprovado"
    elif media >= 7 and media < 10:
        return "Aprovado"
    else:
        return "Parabéns, sua média é 10"

media = calcular_media(notas)
situacao = verificar_situacao(media)
print(f"Situação do aluno: {situacao}, com uma média de {media}")
