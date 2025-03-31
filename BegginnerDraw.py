import tkinter as tk
from tkinter import ttk

# Create The Main Window
window = tk.Tk()

# Canvas
canvas = tk.Canvas(window, width = 600, height = 400)
canvas.pack()

# Draw Line
def draw(event):
    x = event.x
    y = event.y
    canvas.create_oval(x - brush_size/2, y - brush_size/2, x + brush_size/2, y  + brush_size/2, fill = 'black')

def brush_size_adjust(event):
    global brush_size

    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4

    brush_size = max(0, min(brush_size, 50))

brush_size = 4


# Event
canvas.bind("<Motion>", draw)
canvas.bind("<MouseWheel>", brush_size_adjust)

# Run 
window.mainloop()