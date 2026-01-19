import tkinter as tk
import math

class XorCubeJumping:
    def __init__(self, root):
        self.root = root
        self.root.title("Oxidation")
        
        # Tamanho da janela
        self.win_w, self.win_h = 400, 400
        
        # Centralizar a janela inicialmente
        self.screen_w = self.root.winfo_screenwidth()
        self.screen_h = self.root.winfo_screenheight()
        self.pos_x = (self.screen_w // 2) - (self.win_w // 2)
        self.pos_y = (self.screen_h // 2) - (self.win_h // 2)

        self.canvas = tk.Canvas(root, width=self.win_w, height=self.win_h, bg="black", highlightthickness=0)
        self.canvas.pack()

        # Configurações do Cubo 3D
        self.vertices = [[-1,-1,1], [1,-1,1], [1,1,1], [-1,1,1], [-1,-1,-1], [1,-1,-1], [1,1,-1], [-1,1,-1]]
        self.faces = [(0,1,2,3), (1,5,6,2), (5,4,7,6), (4,0,3,7), (0,4,5,1), (3,2,6,7)]
        
        self.angle = 0
        self.time = 0
        self.animate()

    def animate(self):
        self.canvas.delete("all")
        self.time += 0.1
        self.angle += 0.05

        # --- LÓGICA PARA A JANELA PULAR ---
        # Calcula o "salto" usando o valor absoluto do Seno (para sempre subir e bater no chão)
        jump_height = 100 
        current_jump = abs(math.sin(self.time)) * jump_height
        new_y = int(self.pos_y - current_jump)
        
        # Aplica a nova posição à janela do Windows/Linux/Mac
        self.root.geometry(f"{self.win_w}x{self.win_h}+{self.pos_x}+{new_y}")

        # --- RENDERIZAÇÃO DO CUBO ---
        translated_faces = []
        for face in self.faces:
            points = []
            z_sum = 0
            for i in face:
                x, y, z = self.vertices[i]
                # Rotação simples
                nx = x * math.cos(self.angle) - z * math.sin(self.angle)
                nz = x * math.sin(self.angle) + z * math.cos(self.angle)
                ny = y * math.cos(self.angle) - nz * math.sin(self.angle)
                nnz = y * math.sin(self.angle) + nz * math.cos(self.angle)
                
                # Projeção
                f = 200 / (nnz + 4)
                px = nx * f + (self.win_w / 2)
                py = ny * f + (self.win_h / 2)
                points.append((px, py))
                z_sum += nnz
            translated_faces.append((z_sum/4, points))

        # Pintar as faces (Z-order)
        translated_faces.sort(key=lambda x: x[0], reverse=True)

        for _, pts in translated_faces:
            # Lógica XOR para cores RGB baseada no tempo
            r = (int(self.time * 10) ^ 128) % 256
            g = (int(self.angle * 20) ^ 64) % 256
            b = 255 - r
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_polygon(pts, fill=color, outline="white")

        self.root.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    # Remove as bordas da janela para um efeito mais "limpo" (opcional)
    # root.overrideredirect(True) 
    app = XorCubeJumping(root)
    root.mainloop()
