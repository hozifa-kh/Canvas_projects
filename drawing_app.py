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
        self.fill_color = None

        # Adjust The Brush Color  
        colors = ['black','red','blue','green','yellow','orange','pink','brown','lime','violet']
        self.color = tk.StringVar(value = colors[0]) 

        color_frame = ttk.Frame(self.window)
        color_label = ttk.Label(color_frame, text = "Color", font =('Arial',15))
        color_combo = ttk.Combobox(color_frame, values = colors, textvariable = self.color,
                                    font =("Arial",15))

        color_label.pack(side = 'left', padx = 10)
        color_combo.pack(pady = 5)
        color_frame.pack()

        # Create Brush Size Label
        self.width_label = ttk.Label(self.window, text = f"Brush Size: {self.width}", font = 'Arial 10')
        self.width_label.pack()

        # Create a Eraser
        self.eraser_button = tk.Button(self.window, text = "Eraser", bg = 'gray', fg ='white',
                    height = 2, width = 10, font ="Arial 10 bold", border = 0, command = self.eraser)
        self.eraser_button.pack(pady = 30)
        self.eraser_status = False

        # Create Clear Screen Button
        self.clear = ttk.Button(self.window, text = "Clear Screen",
                                command = lambda: self.canvas.delete('all'))
        self.clear.pack()

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

        # Update Brush Size Label
        self.width_label['text'] = f'Brush Size: {self.width}'

    def eraser(self):
        # Toggle The Eraser Mode
        if self.eraser_status:
            self.fill_color = self.color.get()
            self.eraser_button['bg'] = 'gray'

        else:
            self.fill_color = self.canvas['bg']
            self.eraser_button['bg'] = 'red'

        self.eraser_status = not self.eraser_status

    def on_mouse_click(self, event):
        # Start Drawing When Mouse Clicked and Store Position
        self.last_x = event.x
        self.last_y = event.y

    def on_mouse_drag(self, event):
        # Get The Color 
        if self.fill_color != self.canvas['bg']:
            self.fill_color = self.color.get()
        else:
            self.fill_color = self.canvas['bg']

        # Draw Line From The Last Position to The New One
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                        fill = self.fill_color , width = self.width ,smooth = True, capstyle = tk.ROUND)
            self.last_x = event.x
            self.last_y = event.y

    def on_mouse_release(self, event):
        # Stop Drawing When Mouse Button Is Released
        self.last_x, self.last_y = None, None
    
if __name__ == "__main__":
    
    window = tk.Tk()
    app = DrawingApp(window)
    window.mainloop()
