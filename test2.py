import sys
import tkinter
import time



root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

def count():
    timer=5
    while timer>=1:
        timer-=1
        time:q


Button = tkinter.Button(root,text=u'reset',command=count)
Button.pack()

timer=5

static1 = tkinter.Label(text=timer)
static1.pack()

timer-=1
time.sleep(1)

root.mainloop()
