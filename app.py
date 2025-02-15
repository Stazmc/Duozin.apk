import tkinter as tk
import webbrowser
import random
from PIL import Image, ImageTk

def carregar_estilo(arquivo):
    estilos = {}
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            if "=" in linha:
                chave, valor = linha.strip().split("=")
                estilos[chave.strip()] = valor.strip().replace('"', '')
    return estilos

estilo = carregar_estilo("style.css")

def abrir_link():
    webbrowser.open("https://discord.gg/zGFSw5W3")

def mover_botao_nao(event):
    novo_x = random.randint(10, 300)
    novo_y = random.randint(10, 300)
    botao_nao.place(x=novo_x, y=novo_y)

top = tk.Tk()
top.title("Duozin?")
top.geometry("400x400")

top.bg_image = Image.open("N.jpeg")
top.bg_image = top.bg_image.resize((400, 400), Image.LANCZOS)
top.bg_photo = ImageTk.PhotoImage(top.bg_image)

background_label = tk.Label(top, image=top.bg_photo)
background_label.place(relwidth=1, relheight=1)

titulo = tk.Label(top, text="Duozin hoje?", fg="white", bg="black", font=("Arial", 16))
titulo.pack(pady=20)

frame_botoes = tk.Frame(top, bg="black")
frame_botoes.pack()

botao_sim = tk.Button(frame_botoes, text="SIM", command= abrir_link, width=10, height=2)
botao_sim.pack(side=tk.LEFT, padx=10)

botao_nao = tk.Button(frame_botoes, text="NÃO", width=10, height=2)
botao_nao.pack(side= tk.RIGHT, padx=10)
botao_nao.bind("<Enter>", mover_botao_nao)

top.mainloop()