import os,sys,time
import tkinter
import mcpi.minecraft as minecraft
from time import sleep

mc = minecraft.Minecraft.create()

x=0
z=0

gx=4
gz=4

def Reset():

    global x
    global z
    global gx,gz
    x=0
    z=0
    mc.setBlocks(-100,1,-100,100,100,100,0)
    mc.setBlocks(-100,0,-100,100,0,100,2)
    mc.player.setPos(0,1,0)

    mc.setBlocks(-5,0,-5,5,0,5,35,13)
    mc.setBlocks(-5,1,-5,-5,1,5,35,13)
    mc.setBlocks(-5,1,-5,5,1,-5,35,13)
    mc.setBlocks(5,1,5,-5,1,5,35,13)
    mc.setBlocks(5,1,5,5,1,-5,35,13)

    mc.setBlock(gx,0,gz,35,12)

    mc.setBlock(x,0,z,35,14)

def Hello():

    mc.postToChat("Hello Minecraft")


def Go():


    global x
    global z
    mc.setBlock(x,0,z,35,13)
    x+=1
    mc.setBlock(x,0,z,35,14)

def Back():


    global x
    global z
    mc.setBlock(x,0,z,35,13)
    x-=1
    mc.setBlock(x,0,z,35,14)

def Right():


    global x
    global z
    mc.setBlock(x,0,z,35,13)
    z+=1
    mc.setBlock(x,0,z,35,14)

def Left():


    global x
    global z
    mc.setBlock(x,0,z,35,13)
    z-=1
    mc.setBlock(x,0,z,35,14)



def five():


    global x
    global z

    for i in range(5):
        mc.setBlock(x,0,z,35,13)
        x-=1
        mc.setBlock(x,0,z,35,14)
        sleep(1)

def main():

    root = tkinter.Tk()

    mc.postToChat("Hello")

    root.title("Tkinter test")
    root.geometry("640x480")

    Button1 = tkinter.Button(root,text=u'reset',command=Reset)
    Button1.pack()

    Button2 = tkinter.Button(root,text=u'Hello Minecraft',command=Hello)
    Button2.pack()

    Button3 = tkinter.Button(root,text=u'go',command=Go)
    Button3.pack()

    Button4 = tkinter.Button(root,text=u'back',command=Back)
    Button4.pack()

    Button5 = tkinter.Button(root,text=u'left',command=Left)
    Button5.pack()

    Button6 = tkinter.Button(root,text=u'right',command=Right)
    Button6.pack()

    Button7 = tkinter.Button(root,text=u'five',command=five)
    Button7.pack()

    root.mainloop()

if __name__ == "__main__":
    main()


