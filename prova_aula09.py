from tkinter import *

janela = Tk()
janela.title("Conversor de Centímetros para Metros")

def converter():
    centimetros = float(campo_entrada.get())
    metros = centimetros / 100
    campo_saida.delete(0, END)
    campo_saida.insert(0, metros)

rotulo_entrada = Label(janela, text="Centímetros:")
campo_entrada = Entry(janela)
rotulo_saida = Label(janela, text="Metros:")

campo_saida = Entry(janela)
botao_converter = Button(janela, text="Converter", command=converter)

rotulo_entrada.grid(row=0, column=0)
campo_entrada.grid(row=0, column=1)
rotulo_saida.grid(row=1, column=0)
campo_saida.grid(row=1, column=1)
botao_converter.grid(row=2, column=1)

janela.mainloop()
