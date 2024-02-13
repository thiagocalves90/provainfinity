tentativa = 3

for i in range(tentativa):
    senha = input("Digite sua senha: ")
    confirmacao_senha = input("Confirme sua senha: ")
    if senha == confirmacao_senha:
        print("Senha correta. Bem vindo.")
        break
    else:    
        tentativa_restante = tentativa - i - 1
        print(f"Senha incorreta. Você tem {tentativa_restante} até o bloqueio.")

if i == tentativa - 1:
    print(f"Telefone bloquado. Entre em contato com o suporte.")
