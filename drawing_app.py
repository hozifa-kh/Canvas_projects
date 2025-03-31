import tkinter as tk
from tkinter import ttk

class DrawingApp():
    def __init__(self, window):
        self.window = window
        self.window.title("Drawing App")
        self.window.geometry("1000x800")

         # Create Canvas
        self.canvas = tk.Canvas(window, width = 800, height = 600, bg = 'white')
        self.canvas.pack()

        # Initialize Drawing Variables
        self.last_x = None
        self.last_y= None
        self.width = 10

        # Adjust The Brush Color  
        colors = ["black",'red','blue','green','yellow','orange','pink']
        self.color = tk.StringVar(value = colors[0]) 

        color_frame = ttk.Frame(self.window)
        color_label = ttk.Label(color_frame, text = "Color", font =('Arial',15))
        color_combo = ttk.Combobox(color_frame, values = colors, textvariable = self.color,
                                    font =("Arial",15))

        color_label.pack(side = 'left', padx = 10,)
        color_combo.pack(pady = 5)
        color_frame.pack()

        # Check Events
        self.canvas.bind("<Button-1>", self.on_mouse_click)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)
        self.canvas.bind("<MouseWheel>", self.adjust_width)

    def adjust_width(self, event):
        # Adjust The Width Of The Brush By Mouse Wheel
        if event.delta > 0:
            self.width += 4
        else:
            self.width -= 4
            
        # Check That Its Not < 0 or Bigger Than 50
        self.width = max(0, min(self.width, 50))    


    def on_mouse_click(self, event):
        # Start Drawing When Mouse Clicked and Store Position
        self.last_x = event.x
        self.last_y = event.y

    def on_mouse_drag(self, event):
        # Get The Color 
        fill_color = self.color.get()

        # Draw Line From The Last Position to The New One
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                            fill = fill_color, width = self.width ,smooth = True, capstyle = tk.ROUND)
            self.last_x = event.x
            self.last_y = event.y

    def on_mouse_release(self, event):
        # Stop Drawing When Mouse Button Is Released
        self.last_x, self.last_y = None, None
    
if __name__ == "__main__":
    
    window = tk.Tk()
    app = DrawingApp(window)
    window.mainloop()
