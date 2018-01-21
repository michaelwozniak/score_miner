import tkinter as Tk
from tkinter import messagebox
import sys
import os
import csv
from pathlib import Path

# class Model():
#     def __init__(self):


class View():
    def __init__(self, master):

        self.frame = Tk.Frame(master)
        self.logo = Tk.PhotoImage(file='media/logo.png')
        self.logo_label = Tk.Label(master, image=self.logo)
        self.logo_label.pack(side='top')
        self.wc_predictor = Tk.Button(self.frame, text="World Cup 2018 Predictor",padx=5, pady=5)
        self.bl_predictor = Tk.Button(self.frame, text="Bundesliga 2017/2018 Predictor",padx=5, pady=5)
        self.wc_predictor.pack(side="top",fill=Tk.BOTH,padx=5, pady=5)
        self.bl_predictor.pack(side="top",fill=Tk.BOTH,padx=5, pady=5)
        self.nickget = NickGet(master)
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)


class NickGet():
    def __init__(self, root):
        self.frame2 = Tk.Frame(root)
        self.frame2.pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)
        self.wc_label = Tk.Label(self.frame2, text="Please, enter your nickname", padx=5, pady=5)
        self.wc_label.pack(side="top", fill=Tk.BOTH, padx=5, pady=5)
        self.nick_label = Tk.Label(self.frame2, text="Nickname")
        self.nick_entry = Tk.Entry(self.frame2,width=50)
        self.nick_button = Tk.Button(self.frame2, text="Submit")
        self.nick_label.pack(side="left", fill=Tk.BOTH)
        self.nick_entry.pack(side="left", fill=Tk.BOTH)
        self.nick_button.pack(side="left", fill=Tk.BOTH)


class Controller():

    def __init__(self):
        self.root = Tk.Tk()
        self.root.resizable(False, False)
        # self.model = Model()
        self.root.eval('tk::PlaceWindow %s center' % self.root.winfo_pathname(self.root.winfo_id()))
        self.update_datasets()
        self.view = View(self.root)
        self.view.wc_predictor.bind("<Button>",self.choose1)
        self.view.bl_predictor.bind("<Button>",self.choose2)
        self.view.nickget.nick_button.bind("<Button>",self.getentry)

    def update_datasets(self):
        nicknamepath = Path('datasets/nickname.csv')
        if (nicknamepath.exists()):
            os.remove('datasets/nickname.csv')

    def run(self):
        self.root.title("Score miner")
        self.root.deiconify()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

    def getentry(self,event):
        self.playernick = self.view.nickget.nick_entry.get()
        RESULTS = [self.playernick]
        resultFyle = open("datasets/nickname.csv", 'w')
        for r in RESULTS:
            resultFyle.write(r + "\n")
        resultFyle.close()
        messagebox.showinfo("Info", "We saved your nickname!!!")

    def choose1(self,event):
        nicknamepath = Path('datasets/nickname.csv')
        if (nicknamepath.exists()==0):
            messagebox.showerror("Error", "Please, enter your nickname!")
        else:
            os.system('python wp.py')

    def choose2(self,event):
        nicknamepath = Path('datasets/nickname.csv')
        if (nicknamepath.exists() == 0):
            messagebox.showerror("Error", "Please, enter your nickname!")
        else:
            messagebox.showinfo("Info", "Please, give us 15 sec!")
            import bundesliga_part1
            import bundesliga_part2
            import bundesliga_part3
            # we are ignoring warnings :(
            import warnings
            warnings.filterwarnings("ignore")
            bundesliga_part1.bundes1()
            bundesliga_part2.bundes2()
            bundesliga_part3.bundes3()
            os.system('python bl.py')

if __name__ == '__main__':
    start = Controller()
    start.run()
