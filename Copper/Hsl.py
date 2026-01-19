import tkinter as tk
import random

class OxidationPayload:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.config(cursor="none") # Esconde o mouse
        
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        
        # Canvas para desenhar
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg='black', highlightthickness=0)
        self.canvas.pack()
        
        self.t = 0
        self.update_effect()
        
        # Sair com a tecla ESC
        self.root.bind('<Escape>', lambda e: self.root.destroy())

    def update_effect(self):
        # Limpa o canvas para o próximo frame
        self.canvas.delete("all")
        
        # 1. Gerar Padrão XOR Fractal Simplificado
        # Como o Tkinter é lento para pixels individuais, desenhamos retângulos maiores
        size = 20  # Tamanho do "pixel" do fractal
        for x in range(0, self.width, size * 2):
            for y in range(0, self.height, size * 2):
                # Lógica XOR
                val = (x ^ y ^ self.t) % 255
                
                # Ciclo de cores (Tons de Laranja e Amarelo)
                r = val
                g = (val // 2 + (self.t % 100)) % 150
                color = f'#{r:02x}{g:02x}00'
                
                self.canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline="")

        # 2. Texto "Oxidation"
        for _ in range(3):
            tx = random.randint(0, self.width)
            ty = random.randint(0, self.height)
            self.canvas.create_text(
                tx, ty, 
                text="Cu 29", 
                fill="#FF8C00", 
                font=("Times New Roman", random.randint(20, 60)),
                angle=random.randint(0, 360) # Texto em ângulos variados
            )

        self.t += 5
        # Chama a função novamente após 50ms (aprox 20 FPS)
        self.root.after(50, self.update_effect)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = OxidationPayload()
    app.run()
