alunos = {}

while True:
    print("1 - Adicionar um aluno")
    print("2 - Remover um aluno")
    print("3 - Visualizar todos os alunos")
    print("4 - Sair")
    
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        nome = input("Digite o nome do aluno: ")
        matricula = int(input("Digite o número de matrícula do aluno: "))
        alunos[nome] = matricula
    elif opcao == 2:
        matricula = int(input("Digite o número de matrícula do aluno a ser removido: "))
        if matricula in alunos:
            del alunos[matricula]
        else:
            print("Aluno não encontrado.")
    elif opcao == 3:
        if alunos:
            print("Alunos cadastrados:")
            for nome, matricula in alunos.items():
                print(f"{nome} - {matricula}")
        else:
            print("Não há alunos cadastrados.")
    elif opcao == 4:
        break
    else:
        print("Opção inválida.")
    print()
