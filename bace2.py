import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time

li=[0 for i in range(101)]
cnt=1
item_id=0

class Application(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master

class blocks():
    def __init__(self,filename,x,y,tag):
        self.filename=filename
        self.img=Image.open(filename);
        self.img=ImageTk.PhotoImage(self.img)
        self.x=x
        self.y=y
        self.tag=str(tag)

        self.pressed_x = self.pressed_y = 0
        #self.ID=num
        #self.item_id=num

    def setid(self,id):
            self.id=id

    def pressed(self,event):

        global canvas,li,cnt,item_id

        #width,height=self.img.size
        


        if self.id<=3:
            print(self.id)
            li[cnt]=blocks(self.filename,self.x+200,self.y,cnt)
            ID=canvas.create_image(li[cnt].x,li[cnt].y,image=li[cnt].img,tags=li[cnt].tag)
            
            canvas.tag_bind(li[cnt].tag,"<Button-1>",li[cnt].pressed)
            canvas.tag_bind(li[cnt].tag,"<B1-Motion>",li[cnt].dragged)
            li[cnt].setid(cnt+3)

            #canvas.coords(li[cnt].id, li[cnt].x, li[cnt].y)
            cnt+=1
            return
        else:
            print(self.id)   
            #self.pressed_x = event.x
            #self.pressed_y = event.y


        #if self.x<=event.x and event.x<=self.x+width and self.y<=event.y and event.y<=self.y+height:

            #else:
            #item_id=self.id

        
        #else:
        #    self.item_id = canvas.find_closest(event.x, event.y)
        #tag = canvas.gettags(item_id)

        #self.item = canvas.type(tag)
        #print(item)
        #print(tag)




    def dragged1(self,event):
        
        if(self.id<=3): return 

        global li,cnt,item_id
        

        #width,height=self.img.size
        #if self.id<=3:
        #    li[cnt]=blocks(self.filename,self.x+50,self.y)

        #    ID=canvas.create_image(li[cnt].x,li[cnt].y,image=li[cnt].img,tags=cnt)
        #    print(ID)
        #    li[cnt].setid(ID)
        #    cnt+=1


        #print('{0} {1} {2} {3}'.format(self.x,self.y,item_id,self.ID))
        #item_id=self.item_id
        #item_id = canvas.find_closest(event.x, event.y)
        #tag = canvas.gettags(item_id)
        #item = canvas.type(tag) # rectangle image
        self.delta_x = event.x - self.pressed_x
        self.delta_y = event.y - self.pressed_y
        if abs(self.delta_x)>=20: 
            self.delta_x=0
        if abs(self.delta_y)>=20:
            self.delta_y=0
        #print('{0} {1}'.format(self.delta_x,self.delta_y))
        #if item == "rectangle":
        #    x0, y0, x1, y1 = canvas.coords(item_id)
        #    canvas.coords(item_id, x0+delta_x, y0+delta_y, x1+delta_x, y1+delta_y)
        #else:
        #x, y = canvas.coords(item_id)
        self.x+=self.delta_x
        self.y+=self.delta_y
        canvas.coords(self.id, self.x, self.y)

        self.pressed_x = event.x
        self.pressed_y = event.y

    def dragged(self,event):
        global canvas
        x = event.x
        y = event.y
        canvas.coords(self.id,x-15,y-15)

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

def main():



    root.title("test")
    root.minsize(900,900)
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)

    
    mae=blocks('images/mae.png',50,70,"mae")
    migi=blocks('images/migi.png',50,200,"migi")
    end=blocks('images/end.png',50,330,"end")
    global canvas

    #canvas = tk.Canvas(width=100,height=480,bg="white")

    canvas = tk.Canvas(width=400,height=800,bg="white")

    id=canvas.create_image(mae.x,mae.y,image=mae.img,tags=mae.tag)
    mae.setid(id)
    
    id=canvas.create_image(migi.x,migi.y,image=migi.img,tags=migi.tag)
    migi.setid(id)

    id=canvas.create_image(end.x,end.y,image=end.img,tags=end.tag)
    end.setid(id)


        
    #root.protocol("WM_DELETE_WINDOW", on_closing)

    

    canvas.create_line(140,0,140,800,fill='black')

    canvas.place(x=0,y=100)

    canvas.tag_bind(mae.tag,"<Button-1>",mae.pressed)
    canvas.tag_bind(migi.tag,"<Button-1>",migi.pressed)
    canvas.tag_bind(end.tag,"<Button-1>",end.pressed)

    canvas.tag_bind(mae.tag,"<B1-Motion>",mae.dragged)
    canvas.tag_bind(migi.tag,"<B1-Motion>",migi.dragged)
    canvas.tag_bind(end.tag,"<B1-Motion>",end.dragged)

    root.after(10,test)

    root.mainloop()

if __name__=="__main__":
    main()
    
