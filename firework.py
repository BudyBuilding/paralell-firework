import tkinter as tk
import threading
import time
import numpy as np
import random
from datetime import datetime

class FireworkCanvas(tk.Canvas):
    def __init__(self, master, method, **kwargs):
        super().__init__(master, **kwargs)
        self.method = method
        self.bind("<Button-1>", self.show_firework)
        self.times = []

    def show_firework(self, event):
        start_time = time.time()
        if self.method == 'sequential':
            self.sequential_firework(event.x, event.y, start_time)
        elif self.method == 'simd':
            self.simd_firework(event.x, event.y, start_time)
        elif self.method == 'multithreading':
            threading.Thread(target=self.multithreading_firework, args=(event.x, event.y, start_time)).start()

    def draw_particle(self, x, y, dx, dy, color, lifespan):
        for i in range(lifespan):
            x += dx
            y += dy
            alpha = max(0, 255 - int(255 * (i / lifespan)))
            fill_color = self.winfo_rgb(color) + (alpha,)
            self.create_oval(x-2, y-2, x+2, y+2, fill=color, outline=color)
            if i % 10 == 0:  # Update less frequently to avoid too many nested evaluations
                self.update()
            time.sleep(0.01)
        self.delete("all")

    def sequential_firework(self, x, y, start_time):
        particles = 50
        for _ in range(particles):
            angle = random.uniform(0, 2 * np.pi)
            speed = random.uniform(2, 5)
            dx = speed * np.cos(angle)
            dy = speed * np.sin(angle)
            color = random.choice(['red', 'yellow', 'orange'])
            threading.Thread(target=self.draw_particle, args=(x, y, dx, dy, color, 100)).start()
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.times.append(elapsed_time)
        self.print_times(elapsed_time)

    def simd_firework(self, x, y, start_time):
        particles = 50
        angles = np.random.uniform(0, 2 * np.pi, particles)
        speeds = np.random.uniform(2, 5, particles)
        dxs = speeds * np.cos(angles)
        dys = speeds * np.sin(angles)
        colors = np.random.choice(['blue', 'purple', 'cyan'], particles)
        for dx, dy, color in zip(dxs, dys, colors):
            threading.Thread(target=self.draw_particle, args=(x, y, dx, dy, color, 100)).start()
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.times.append(elapsed_time)
        self.print_times(elapsed_time)

    def multithreading_firework(self, x, y, start_time):
        def draw():
            particles = 50
            for _ in range(particles):
                angle = random.uniform(0, 2 * np.pi)
                speed = random.uniform(2, 5)
                dx = speed * np.cos(angle)
                dy = speed * np.sin(angle)
                color = random.choice(['green', 'lime', 'magenta'])
                threading.Thread(target=self.draw_particle, args=(x, y, dx, dy, color, 100)).start()
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.times.append(elapsed_time)
            self.print_times(elapsed_time)
        threading.Thread(target=draw).start()

    def print_times(self, elapsed_time):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        avg_time = sum(self.times) / len(self.times) if self.times else 0
        print(f"{self.method} method took {elapsed_time:.4f} seconds at {current_time}")
        print(f"{self.method} average time: {avg_time:.4f} seconds")

def print_averages(canvases):
    sequential_times = canvases.times
    simd_times = canvases.times
    multithreading_times = canvases.times

    sequential_avg = sum(sequential_times) / len(sequential_times) if sequential_times else 0
    simd_avg = sum(simd_times) / len(simd_times) if simd_times else 0
    multithreading_avg = sum(multithreading_times) / len(multithreading_times) if multithreading_times else 0
    overall_avg = (sequential_avg + simd_avg + multithreading_avg) / 3

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Sequential average time: {sequential_avg:.4f} seconds at {current_time}")
    print(f"SIMD average time: {simd_avg:.4f} seconds at {current_time}")
    print(f"Multithreading average time: {multithreading_avg:.4f} seconds at {current_time}")
    print(f"Overall average time: {overall_avg:.4f} seconds at {current_time}")

root = tk.Tk()
root.geometry("900x300")
root.configure(bg='black')

frame1 = tk.Frame(root, width=300, height=300, bg='black')
frame1.pack(side="left")
frame2 = tk.Frame(root, width=300, height=300, bg='black')
frame2.pack(side="left")
frame3 = tk.Frame(root, width=300, height=300, bg='black')
frame3.pack(side="left")

canvas1 = FireworkCanvas(frame1, method='sequential', bg='black')
canvas1.pack(fill="both", expand=True)
canvas2 = FireworkCanvas(frame2, method='simd', bg='black')
canvas2.pack(fill="both", expand=True)
canvas3 = FireworkCanvas(frame3, method='multithreading', bg='black')
canvas3.pack(fill="both", expand=True)

canvases = [canvas1, canvas2, canvas3]

# Print averages every 10 seconds
def periodic_print():
    print_averages(canvases)
    root.after(10000, periodic_print)

root.after(10000, periodic_print)
root.mainloop()
