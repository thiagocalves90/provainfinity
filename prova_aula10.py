import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Tela de Login")

rotulo_email = tk.Label(janela, text="E-mail:")
rotulo_email.grid(row=0, column=0)
campo_email = tk.Entry(janela)
campo_email.grid(row=0, column=1)

rotulo_senha = tk.Label(janela, text="Senha:")
rotulo_senha.grid(row=1, column=0)
campo_senha = tk.Entry(janela, show="*")
campo_senha.grid(row=1, column=1)

def verificar_login():
    email = campo_email.get()
    senha = campo_senha.get()
    if "@" not in email:
        tk.messagebox.showerror("Erro", "E-mail inválido")
        return
    if len(senha) < 6:
        tk.messagebox.showerror("Erro", "Senha muito curta")
        return
    tk.messagebox.showinfo("Sucesso", "Login efetuado com sucesso")

botao_login = tk.Button(janela, text="Login", command=verificar_login)
botao_login.grid(row=2, column=1)

janela.mainloop()
