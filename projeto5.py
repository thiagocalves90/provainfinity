import venv

venv.create("venv")

tarefas = {}

class Tarefa:
    def __init__(self, nome, descricao, prioridade, categoria):
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade
        self.categoria = categoria
        self.concluida = False

def adicionar_tarefa():
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    prioridade = int(input("Prioridade da tarefa (1-5): "))
    categoria = input("Categoria da tarefa: ")
    tarefa = Tarefa(nome, descricao, prioridade, categoria)
    tarefas[nome] = tarefa

def listar_tarefas():
    for tarefa in tarefas.values():
        print(f"{tarefa.nome} - {tarefa.descricao} - {tarefa.prioridade} - {tarefa.categoria} - {'Concluída' if tarefa.concluida else 'Pendente'}")

def marcar_como_concluida():
    nome = input("Nome da tarefa a ser marcada como concluída: ")
    if nome in tarefas:
        tarefas[nome].concluida = True
    else:
        print("Tarefa não encontrada")

def exibir_por_prioridade():
    tarefas_ordenadas = sorted(tarefas.values(), key=lambda t: t.prioridade)
    for tarefa in tarefas_ordenadas:
        print(f"{tarefa.nome} - {tarefa.descricao} - {tarefa.prioridade} - {tarefa.categoria} - {'Concluída' if tarefa.concluida else 'Pendente'}")

def exibir_por_categoria():
    categorias = set(tarefa.categoria for tarefa in tarefas.values())
    for categoria in categorias:
        print(f"Categoria: {categoria}")
        for tarefa in tarefas.values():
            if tarefa.categoria == categoria:
                print(f"\t{tarefa.nome} - {tarefa.descricao} - {tarefa.prioridade} - {'Concluída' if tarefa.concluida else 'Pendente'}")

while True:
    comando = input("Comando (adicionar, listar, marcar, prioridade, categoria, sair): ")
    if comando == "adicionar":
        adicionar_tarefa()
    elif comando == "listar":
        listar_tarefas()
    elif comando == "marcar":
        marcar_como_concluida()
    elif comando == "prioridade":
        exibir_por_prioridade()
    elif comando == "categoria":
        exibir_por_categoria()
    elif comando == "sair":
        break
