import tkinter as tk
from tkinter import messagebox
import random

class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação")
        self.root.geometry("500x400")
        self.root.configure(bg = '#ADD8E6')

        # Gerar o número secreto entre 1 e 100
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0

        # Interface
        self.label_instrucao = tk.Label(root, text="Tente adivinhar o número (1 a 100):")
        self.label_instrucao.pack(pady=10)

        self.entrada_palpite = tk.Entry(root)
        self.entrada_palpite.pack(pady=5)

        self.botao_verificar = tk.Button(root, text="Verificar", command=self.verificar_palpite)
        self.botao_verificar.pack(pady=10)

        self.label_feedback = tk.Label(root, text="", fg="blue")
        self.label_feedback.pack(pady=5)

    def verificar_palpite(self):
        try:
            palpite = int(self.entrada_palpite.get())
            self.tentativas += 1

            if palpite < self.numero_secreto:
                self.label_feedback.config(text="Muito baixo! Tente novamente.", fg="red")
            elif palpite > self.numero_secreto:
                self.label_feedback.config(text="Muito alto! Tente novamente.", fg="red")
            else:
                messagebox.showinfo("Parabéns!", f"Você acertou em {self.tentativas} tentativas!")
                self.reiniciar_jogo()
        except ValueError:
            messagebox.showwarning("Erro", "Por favor, digite um número válido.")

    def reiniciar_jogo(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
        self.entrada_palpite.delete(0, tk.END)
        self.label_feedback.config(text="Novo jogo iniciado!")

    def carregar_imagens(self):
        # 📁 Pasta das imagens (crie uma pasta "imagens")
        pasta_imagens = 'baixados.jpg'    

# Inicialização do app
if __name__ == "__main__":
    root = tk.Tk()
    app = JogoAdivinhacao(root)
    root.mainloop()