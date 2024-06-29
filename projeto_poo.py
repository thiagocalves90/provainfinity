class Livro:
    def __init__(self, titulo, autor, id, status_emprestimo):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.status_emprestimo = status_emprestimo
class Membro:
    def __init__(self, nome, numero_membro, historico_emprestimos):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_emprestimos = historico_emprestimos
class Biblioteca:
    def __init__(self, catalogo_livros, registro_membros):
        self.catalogo_livros = catalogo_livros
        self.registro_membros = registro_membros
   
    def adicionar_livro(self, livro):
        self.catalogo_livros.append(livro)

    def adicionar_membro(self, membro):
        self.registro_membros.append(membro)

    def emprestar_livro(self, membro, livro):
        if livro.status_emprestimo == "Disponível":
            livro.status_emprestimo = "Emprestado"
            membro.historico_emprestimos.append(livro)

    def devolver_livro(self, livro):
        livro.status_emprestimo = "Disponível"

    def pesquisar_livro(self, criterio, valor):
        if criterio == "titulo":
            for livro in self.catalogo_livros:
                if livro.titulo == valor:
                    return livro
        elif criterio == "autor":
            for livro in self.catalogo_livros:
                if livro.autor == valor:
                    return livro
        elif criterio == "id":
            for livro in self.catalogo_livros:
                if livro.id == valor:
                    return livro
        else:
            return None
from classe_biblioteca import *
from classe_membro import *
from classe_livro import *

biblioteca = Biblioteca([], [])

while True:
    comando = input("Digite um comando (adicionar livro, adicionar membro, emprestar livro, devolver livro, pesquisar livro, sair): ")
    if comando == "adicionar livro":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        id = input("Digite o ID do livro: ")
        status_emprestimo = input("Digite o status de empréstimo do livro (Disponível/Emprestado): ")
        livro = Livro(titulo, autor, id, status_emprestimo)
        biblioteca.adicionar_livro(livro)
    elif comando == "adicionar membro":
        nome = input("Digite o nome do membro: ")
        numero_membro = input("Digite o número de membro: ")
        historico_emprestimos = []
        membro = Membro(nome, numero_membro, historico_emprestimos)
        biblioteca.adicionar_membro(membro)
    elif comando == "emprestar livro":
        numero_membro = input("Digite o número de membro: ")
        id_livro = input("Digite o ID do livro: ")
        membro = biblioteca.registro_membros[numero_membro]
        livro = biblioteca.catalogo_livros[id_livro]
        biblioteca.emprestar_livro(membro, livro)
    elif comando == "devolver livro":
        id_livro = input("Digite o ID do livro: ")
        livro = biblioteca.catalogo_livros[id_livro]
        biblioteca.devolver_livro(livro)
    elif comando == "pesquisar livro":
        criterio = input("Digite o critério de pesquisa (titulo/autor/id): ")
        valor = input("Digite o valor da pesquisa: ")
        livro = biblioteca.pesquisar_livro(criterio, valor)
        if livro:
            print(f"Livro encontrado: {livro.titulo} - {livro.autor} - {livro.id} - {livro.status_emprestimo}")
        else:
            print("Livro não encontrado")
    elif comando == "sair":
        break
    else:
        print("Comando inválido")
