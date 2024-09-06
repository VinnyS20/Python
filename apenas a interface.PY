import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    texto = entrada.get()  # Obtém o texto da entrada
    messagebox.showinfo("Mensagem", f"Você digitou: {texto}")

janela = tk.Tk()
janela.title("Interface Gráfica Simples")

rotulo = tk.Label(janela, text="Digite algo:")
rotulo.pack(pady=10)

entrada = tk.Entry(janela)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Mostrar Mensagem", command=mostrar_mensagem)
botao.pack(pady=10)

janela.mainloop()