def AdicionarAluno():
    numero_matricula = input("Informe o número de matrícula do aluno: ")
    nome = input("Informe o nome do aluno: ")
    
    alunos[numero_matricula] = nome
    
    print(f"Aluno adicionado com sucesso! {nome} - {numero_matricula}")

def RemoverAluno():
    numero_matricula = input("Infome o número de matrícula do aluno que deseja remover: ")
    
    if numero_matricula in alunos:
        del alunos[numero_matricula]
        print(f"Aluno removido com sucesso! {numero_matricula}")
    else:
        print("Aluno não encontrado.")

def AtualizarAluno():
    numero_matricula = input("Informe o número de matrícula do aluno que deseja atualizar: ")
    
    if numero_matricula in alunos:
        nome = input("Informe o novo nome do aluno: ")
        alunos[numero_matricula] = nome
        print(f"Aluno atualizado com sucesso! {nome} - {numero_matricula}")
    else:
        print("Aluno não encontrado.")

def VerAlunos():
    print("Alunos cadastrados:")
    for numero_matricula, nome in alunos.items():
        print(f"{numero_matricula} - {nome}")

alunos = {}

while True:
    print("Menu:")
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Atualizar aluno")
    print("4 - Ver alunos")
    print("5 - Sair")
    
    opcao = input("Informe a opção desejada: ")
    
    if opcao == "1":
        AdicionarAluno()
    elif opcao == "2":
        RemoverAluno()
    elif opcao == "3":
        AtualizarAluno()
    elif opcao == "4":
        VerAlunos()
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")
