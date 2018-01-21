from tkinter import *

top = Tk()
top.title("Bundesliga predictor")
top.resizable(False, False)
photo = PhotoImage(file="media/bl_logo.png")
label = Label(top,image=photo)
label.image = photo
label.pack()


def new_winF2():
    newwin = Toplevel(top)
    newwin.resizable(False, False)
    photo = PhotoImage(file="media/bundes1.png")
    label = Label(newwin, image=photo)
    label.image = photo
    label.pack(side=TOP)

def new_winF():
    newwin = Toplevel(top)
    newwin.resizable(False, False)
    w = Label(newwin, text="TABLE WITH RESULTS FROM AUTUMN ROUND WITH PREDICTED RESULTS FROM SPRING ROUND GAMEWEEK BY GAMEWEEK")
    w.pack()
    photo = PhotoImage(file="media/bundes2.png")
    label = Label(newwin, image=photo)
    label.image = photo
    label.pack(side=TOP)
    z = Label(newwin, text="ACTUAL BUNDESLIGA TABLE")
    z.pack()
    photo2 = PhotoImage(file="media/bundes3.png")
    label2 = Label(newwin, image=photo2)
    label2.image = photo2
    label2.pack(side=TOP)

button1 = Button(top, text ="Whole season 2017/2018", command=new_winF2)
button1.pack(side=TOP,fill=BOTH, pady=5)
button2 = Button(top, text ="Round by round predictor - LIVE", command=new_winF)
button2.pack(side=TOP,fill=BOTH, pady=5)
button3 = Button(top, text ="Exit",command=quit)
button3.pack(side=TOP,fill=BOTH, pady=5)

top.mainloop()