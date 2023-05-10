from tkinter import *
from random import *
from tkinter import messagebox
win=Tk()
win.geometry("350x380")
win.title("Game-Paper rock scissors")
win.iconbitmap("C:/Users/Саврон/Desktop/my_project/t_k_k_game/prs.ico")
win
sr=0
sr1=0
c=0
def pr():
    global sr,sr1,lp,lp1,lp2,c
    c+=1
    s=['paper','rock','scissors']
    b=sample(s,1)
    d={"scissors":False,"paper":'Draw',"rock":True}
    b=b[0]
    if d[b]=='Draw':
        lp['text']='Paper'
        lp1['text']='Paper'
        lp2['text']='Draw'
    elif d[b]:
        lp['text']='Paper'
        lp1['text']='Rock'
        lp2['text']='Player'
        sr+=1
    else:
        lp['text']='Paper'
        lp1['text']='Scissors'
        lp2['text']='BOT'
        sr1+=1
    end(c)
def rk():
    global sr,sr1,lp,lp1,lp2,c
    c+=1
    s=['paper','rock','scissors']
    b=sample(s,1)
    d={"scissors":True,"paper":False,"rock":'Draw'}
    b=b[0]
    if d[b]=='Draw':
        lp['text']='Rock'
        lp1['text']='Rock'
        lp2['text']='Draw'
    elif d[b]:
        lp['text']='Rock'
        lp1['text']='Scissors'
        lp2['text']='Player'
        sr+=1
    else:
        lp['text']='Rock'
        lp1['text']='Paper'
        lp2['text']='BOT'
        sr1+=1
    end(c)
def sc():
    global sr,sr1,lp,lp1,lp2,c
    c+=1
    s=['paper','rock','scissors']
    b=sample(s,1)
    d={"scissors":'Draw',"paper":True,"rock":False}
    b=b[0]
    if d[b]=='Draw':
        lp['text']='Scissors'
        lp1['text']='Scissors'
        lp2['text']='Draw'
    elif d[b]:
        lp['text']='Scissors'
        lp1['text']='Paper'
        lp2['text']='Player'
        sr+=1
    else:
        lp['text']='Scissors'
        lp1['text']='Rock'
        lp2['text']='BOT'
        sr1+=1
    end(c)
def nextt():
    global lp,lp1,lp2
    bt["state"]=NORMAL
    bt1["state"]=NORMAL
    bt2["state"]=NORMAL
    lp['text']='unknown'
    lp1['text']='unknown'
    lp2['text']='unknown'
    Label(text=f"Score player:  {sr}",bg='#26262e',fg="white",font=("Arial", 14)).place(x=5,y=260)
    Label(text=f"Score BOT:  {sr1}",bg='#26262e',fg="white",font=("Arial", 14)).place(x=5,y=300)
lb=Label(text="Round").place(x=5,y=5,height=25,width=50)
ent=Entry(win)
ent.place(x=60,y=5,height=25,width=240)
def end(c):
    k=int(ent.get())
    if c==k:
        if sr>sr1:
            messagebox.showinfo('Winner!',"You Won!")
        elif sr<sr1:
            messagebox.showinfo('Winner!',"You Lose")
        else:
            messagebox.showinfo('Winner!',"Draw")
        bt["state"]=DISABLED
        bt1["state"]=DISABLED
        bt2["state"]=DISABLED
        quit()
lb1=Label(text="player",bg='#26262e',fg="white",font=("Arial", 14))
lb1.place(x=5,y=50)
lb2=Label(text="BOT",bg='#26262e',fg="white",font=("Arial", 14))
lb2.place(x=5,y=90)
lb3=Label(text="Winner",bg='#26262e',fg="white",font=("Arial", 14))
lb3.place(x=5,y=130)
btn=Button(text="GO!",command=nextt).place(x=305,y=5,height=25,width=45)
imagel=PhotoImage(file="paper.png")
bt1=Button(win,image=imagel,command=pr,state=DISABLED)
bt1.place(x=5,y=170)
lp=Label(text="unknown",bg='#26262e',fg="white",font=("Arial", 14))
lp.place(x=110,y=50)
lp1=Label(text="unknown",bg='#26262e',fg="white",font=("Arial", 14))
lp1.place(x=110,y=90)
lp2=Label(text="unknown",bg='#26262e',fg="white",font=("Arial", 14))
lp2.place(x=110,y=130)
bl=Button(text='next',command=nextt).place(x=215,y=130)
image=PhotoImage(file="rock.png")
bt=Button(win,image=image,command=rk,state=DISABLED)
bt.place(x=110,y=170)
image1=PhotoImage(file="scissors.png")
bt2=Button(win,image=image1,command=sc,state=DISABLED)
bt2.place(x=215,y=170)
Label(text=f"Score player:  {sr}",bg='#26262e',fg="white",font=("Arial", 14)).place(x=5,y=260)
Label(text=f"Score BOT:  {sr1}",bg='#26262e',fg="white",font=("Arial", 14)).place(x=5,y=300)
win.config(bg='#26262e')
win.update()
win.resizable(False,False)
win.mainloop()
