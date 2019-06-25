import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import time



class Application(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        



pressed_x = pressed_y = 0
item_id = -1
def pressed(event):
    global pressed_x, pressed_y, item_id,canvas 
    item_id = canvas.find_closest(event.x, event.y)
    tag = canvas.gettags(item_id)

    item = canvas.type(tag)
    #print(item)
    #print(tag)
    pressed_x = event.x
    pressed_y = event.y

def dragged(event):
    global pressed_x, pressed_y, item_id,canvas
    #item_id = canvas.find_closest(event.x, event.y)
    #tag = canvas.gettags(item_id)
    #item = canvas.type(tag) # rectangle image
    delta_x = event.x - pressed_x
    delta_y = event.y - pressed_y
    #if item == "rectangle":
    #    x0, y0, x1, y1 = canvas.coords(item_id)
    #    canvas.coords(item_id, x0+delta_x, y0+delta_y, x1+delta_x, y1+delta_y)
    #else:
    x, y = canvas.coords(item_id)
    canvas.coords(item_id, x+delta_x, y+delta_y)
    pressed_x = event.x
    pressed_y = event.y




def main():
    root=tk.Tk()
    app = Application(master=root)

    
    root.title("test")
    root.minsize(900,900)
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)

    img=Image.open('mae.png')
    img=ImageTk.PhotoImage(img)

    global canvas
    
    #canvas = tk.Canvas(width=100,height=480,bg="white")

    canvas = tk.Canvas(width=400,height=800,bg="white")

    img=Image.open('mae.png')
    img=ImageTk.PhotoImage(img)
    canvas.create_image(50,70,image=img,tags="mae")

    im=Image.open('migi.png');
    im=ImageTk.PhotoImage(im);
    
    canvas.create_image(50,200,image=im,tags="migi")

    #canvas.create_line(140,0,140,800,fill='black')
    
    canvas.place(x=0,y=100)

    canvas.tag_bind("mae","<B1-Motion>",pressed)
    canvas.tag_bind("migi","<B1-Motion>",pressed)

    canvas.tag_bind("mae","<B1-Motion>",dragged)
    canvas.tag_bind("migi","<B1-Motion>",dragged)

    root.mainloop()

if __name__=="__main__":
    main()
