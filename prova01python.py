email_cadastrado = 'usuario@email.com'
senha_cadastrado = 'senha123'

while True:
    email_usuario = input('Digite o e-mail: ')
    senha_usuario = input('Digite a senha: ')
    if email_cadastrado == email_usuario and senha_cadastrado == senha_usuario:
        print('Você acertou, bem vindo!')
        break
    else:
        print('Você errou, tente novamente!')
