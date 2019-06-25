#import tkinter
#from PIL import Image,ImageTk
from tkinter import *
from tkinter import ttk
import mcpi.minecraft as minecraft



def main():


    root = Tk()

    
    root.title("Tkinter test")
    root.geometry("640x480")
    root.resizable(1,1)

    textFrame = Frame(root,width=100,height=480, bg="white")
    textFrame.place(x=0,y=100)
    
    textFrame2 = Frame(root,width=200,height=480,bg="white")
    textFrame2.place(x=200,y=100)

    icon=PhotoImage(file='telesa.png')

    GoButton = ttk.Button(root,image=icon)
    GoButton.place(x=420,y=220)

    
    root.mainloop() 

if __name__== "__main__":
        main()
