import tkinter as tk
from tkinter import ttk

# Set Main Window
window = tk.Tk()
window.geometry("800x500")

# Canvas
canvas = tk.Canvas(window, bg = 'white', width = 600, height = 400)
canvas.pack()

canvas.create_polygon((0,400, 300,0, 600,400), fill = 'orange')
canvas.create_line(110,250,480,250)
canvas.create_line(300,250,300,400)
canvas.create_text(300,200, text = "W" , font = ('Ariel',50))
canvas.create_text(210,320, text = "M" , font = ('Ariel',50))
canvas.create_text(400,320, text = "g" , font = ('Ariel',50))
canvas.create_text(300,320, text = "x" , font = ('Ariel',50))

# Run
window.mainloop()