from tkinter import *
import random
from tkinter import messagebox

screen=Tk()
screen.geometry("400x600")
screen.title("Colour game")
screen.configure(bg="black")
s=0
timeLeft=30
def start(event):
    t2.configure(text="")
    if timeLeft==30:
        countdown()
    nextcolor()

def nextcolor():
    global s
    global timeLeft

    if timeLeft>0:
        i.focus_set()
        if i.get().lower()==colours[1].lower():
            s+=1
        i.delete(0,END)
        random.shuffle(colours)
        tex.configure(fg=str(colours[1]),bg="black",text=str(colours[0]))
        score=Label(screen,text="score:"+str(s),font=("Arial",15),fg="red",bg="black")
        score.place(x=450,y=250)
    if timeLeft==0:
         messagebox.showinfo("over","your score is "+str(s))
def countdown():
    global timeLeft

    if timeLeft>0:
        timeLeft-=1
        tm=Label(screen,text="time left : "+ str(timeLeft),font=("Arial",15),fg="red",bg="black")
        tm.place(x=450,y=170)
        tm.after(1000,countdown)
        
colours=["red","blue","yellow","white","brown","coral","magenta","violet","pink","green"]
s=0
t=Label(screen,text="Please type the color name not the word text",font=("ArialBold",19),fg="white",bg="black")
t.place(x=300,y=20)
t2=Label(screen,text="PRESS ENTER TO START",font=("ArialBold",15),fg="white",bg="black")
t2.place(x=400,y=100)
i=Entry(screen,font=("Arial",17),fg="black",width=10)
i.place(x=490,y=550)

tex=Label(screen,font=("Arial",100))
tex.place(x=450,y=350)

screen.bind("<Return>",start)

i.focus_set()
screen.mainloop()
