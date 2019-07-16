#-*-coding:euc-jp-*-

import mcpi.minecraft as minecraft
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from time import sleep

li=[0 for i in range(101)]
mp=[[0 for i in range(3)]for i in range(8)]
cnt=1
item_id=0

mc = minecraft.Minecraft.create()

class Application(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master

class blocks():
    def __init__(self,filename,x,y,tag,kind):
        self.filename=filename
        self.img=Image.open(filename);
        self.img=ImageTk.PhotoImage(self.img)
        self.x=x
        self.y=y
        if kind==1:
            self.dx=50
            self.dy=70
        elif kind==2:
            self.dx=50
            self.dy=200
        else:
            self.dx=50
            self.dy=330
        
        self.tag=str(tag)
        self.flag=False
        self.kind=kind

        self.pressed_x = self.pressed_y = 0

        ID=canvas.create_image(x,y,image=self.img,tags=tag)
        print(ID)
        self.setid(ID)

        #canvas.tag_bind(li[cnt].tag,"<Button-1>",li[cnt].pressed)
        canvas.tag_bind(self.tag,"<B1-Motion>",self.dragged)
        canvas.tag_bind(self.tag,"<ButtonRelease-1>",self.Released)

        #self.ID=num
        #self.item_id=num

    def setid(self,id):
            self.id=id


    def dragged(self,event):
        global canvas,li,cnt
        x = event.x
        y = event.y
        canvas.coords(self.id,x,y)
        print(str(x)+" "+str(y))
        #if x>=140 and self.flag==False:
        #    li[cnt]=blocks(self.filename,self.dx,self.dy,cnt,self.kind)

            #canvas.tag_bind(li[cnt].tag,"<B1-Motion>",li[cnt].dragged)
        #    cnt+=1

        #    self.flag=True
        #elif x<140:
            
    def Released(self,event):
        
        global canvas,li,cnt

        x = event.x
        y = event.y
        #if x-50>=100:
            
        if x>=100:
            if self.flag==False:
                li[cnt]=blocks(self.filename,self.dx,self.dy,cnt,self.kind)
                self.flag=True
                cnt+=1
            nx=(int)(x/100)*100
            ny=(int)(y/100)*100
            print(str(nx)+" "+str(ny))
            if mp[(int)(ny/100)][(int)(nx/100)-1]==0:
                mp[(int)(self.y/100)][(int)(self.x/100)-1]=0
                self.x=nx+50
                self.y=ny+50
                mp[(int)(ny/100)][(int)(nx/100)-1]=self.kind
                
            canvas.coords(self.id,self.x,self.y)

            
        elif x<100:
            mp[(int)(self.y/100)][(int)(self.x/100)-1]=0
            canvas.coords(self.id,self.dx,self.dy)    

root=tk.Tk()
app = Application(master=root)

def on_closing():

    if messagebox.askokcancel("Quit","Quit?"):
        root.destroy()

def test():
    global cnt
    global canvas,li

    for i in range(1,cnt):
        
        #ID=canvas.create_image(li[i].x,li[i].y,image=li[i].img,tags=li[i].tag)
        #li[i].setid(ID)
        canvas.tag_bind(li[i].tag,"<Button-1>",li[i].pressed)
        canvas.tag_bind(li[i].tag,"<B1-Motion>",li[i].dragged)
        
    root.after(10,test)

def start():
    global mp,mc
    sclipt=[0 for i in range(0,24)]
    c=0
    direc='n'
    print(mp)
    for i in range(3):
        for j in range(8):
            print(str(i)+" "+str(j))
            sclipt[c]=mp[j][i]
            c+=1

    
    x=0
    z=0
    mc.setBlock(x,0,z,35,14)
    for i in range(24):
        if sclipt[i]==1:
            mc.setBlock(x,0,z,35,13)
            if direc=='n':
                x+=1
            elif direc=='s':
                x-=1
            elif direc=='e':
                z+=1
            elif direc=='w':
                z-=1
            mc.setBlock(x,0,z,35,14)
        elif sclipt[i]==2:
            if direc=='n':
                direc='e'
            elif direc=='e':
                direc='s'
            elif direc=='s':
                direc='w'
            elif direc=='w':
                direc='n'
        elif sclipt[i]==0 or sclipt[i]==3:
            break
        sleep(0.5)


    print("実行完了")

def main():

    mc.postToChat("Hello")

    root.title("test")
    root.minsize(900,900)
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)

    
    #mae=blocks('images/mae.png',50,70,"mae")
    #migi=blocks('images/migi.png',50,200,"migi")
    #end=blocks('images/end.png',50,330,"end")
    global canvas,li,cnt

    #canvas = tk.Canvas(width=100,height=480,bg="white")

    canvas = tk.Canvas(width=400,height=800,bg="white")



    li[cnt]=blocks('images/mae.png',50,70,cnt,1)
    li[cnt+1]=blocks('images/migi.png',50,200,cnt+1,2)
    li[cnt+2]=blocks('images/end.png',50,330,cnt+2,3)
    cnt+=14

    #root.protocol("WM_DELETE_WINDOW", on_closing)

    

    canvas.create_line(100,0,100,800,fill='black')
    canvas.create_line(200,0,200,800,fill='gray')
    canvas.create_line(300,0,300,800,fill='gray')
    canvas.create_line(400,0,400,800,fill='gray')

    for i in range(1,8):
        canvas.create_line(100,100*i,400,100*i,fill='gray')

    canvas.place(x=0,y=100)

    Button = tk.Button(text=u'スタート',command=start)

    Button.place(x=600,y=400)

    #canvas.tag_bind(mae.tag,"<Button-1>",mae.pressed)
    #canvas.tag_bind(migi.tag,"<Button-1>",migi.pressed)
    #canvas.tag_bind(end.tag,"<Button-1>",end.pressed#)

    #canvas.tag_bind(mae.tag,"<B1-Motion>",mae.dragged)
    #canvas.tag_bind(migi.tag,"<B1-Motion>",migi.dragged)
    #canvas.tag_bind(end.tag,"<B1-Motion>",end.dragged)

    #root.after(10,test)

    root.mainloop()


if __name__=="__main__":
    main()
