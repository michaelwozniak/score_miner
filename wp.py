import tkinter as Tk
from tkinter import messagebox
import sys
import os
import csv
import pandas as pd
from pathlib import Path
import webbrowser


# class Model():
#     def __init__(self):


class View():
    def __init__(self, master):

        self.frame = Tk.Frame(master)
        self.logo = Tk.PhotoImage(file='media/wc_logo.png')
        self.logo_label = Tk.Label(master, image=self.logo)
        self.logo_label.pack(side='top')
        self.wc_predictor = Tk.Button(self.frame, text="Start predictor", padx=5, pady=5)
        self.wc_predictor.pack(side="top",fill=Tk.BOTH, padx=10,pady=10)
        self.formsgoogle = FormsGoogle(master)
        self.nickget = NickGet(master)
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

class NickGet():
    def __init__(self, root):
        self.frame2 = Tk.Frame(root)
        self.frame2.pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)
        self.wc_label = Tk.Label(self.frame2, text="Please, enter your country (participant of WC 2018)", padx=5, pady=5)
        self.wc_label.pack(side="top", fill=Tk.BOTH, padx=10, pady=10)
        self.nick_label = Tk.Label(self.frame2, text="Country")
        self.nick_entry = Tk.Entry(self.frame2,width=50)
        self.nick_button = Tk.Button(self.frame2, text="Submit")
        self.nick_label.pack(side="left", fill=Tk.BOTH)
        self.nick_entry.pack(side="left", fill=Tk.BOTH)
        self.nick_button.pack(side="left", fill=Tk.BOTH)

class FormsGoogle():
    def __init__(self, root):
        self.frame3 = Tk.Frame(root)
        self.frame3.pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)
        self.wc_label = Tk.Label(self.frame3, text="Please, fill in the doc", padx=5, pady=5)
        self.wc_label.pack(side="top", fill=Tk.BOTH, padx=10, pady=10)
        self.nick_button = Tk.Button(self.frame3, text="Fill in",padx=5, pady=5)
        self.nick_button.pack(side="bottom", fill=Tk.BOTH,padx=5, pady=5)


class Controller():

    def __init__(self):
        self.root = Tk.Tk()
        self.root.resizable(False, False)
        # self.model = Model()
        self.root.eval('tk::PlaceWindow %s center' % self.root.winfo_pathname(self.root.winfo_id()))
        self.update_datasets()
        self.view = View(self.root)
        self.view.wc_predictor.bind("<Button>",self.choose1)
        self.view.nickget.nick_button.bind("<Button>",self.getentry)
        self.view.formsgoogle.nick_button.bind("<Button>",self.open_forms)

    def update_datasets(self):
        nicknamepath = Path('datasets/check_if_filled_in.csv')
        if (nicknamepath.exists()):
             os.remove('datasets/check_if_filled_in.csv')

    def open_forms(self,event):
        nicknamepath = Path('datasets/check_if_filled_in.csv')
        if (nicknamepath.exists() == False):
            webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLSdcvghi9DnVhmTx9a3IlHk2N33wNwTsnv4mNst7ZV4D7PwA0Q/viewform')
            checker = "checking"
            temp = [checker]
            resultFyle = open("datasets/check_if_filled_in.csv", 'w')
            for r in temp:
                resultFyle.write(r + "\n")
            resultFyle.close()
        else:
            messagebox.showerror("Error", "You have already filled in this doc!")

    def run(self):
        self.root.title("Score miner")
        self.root.deiconify()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

    def getentry(self,event):
        self.playernick = self.view.nickget.nick_entry.get()
        RESULTS = [self.playernick]
        possible_countries = pd.read_csv('datasets/skills.csv', sep=';')
        a = possible_countries["Team"]
        for i in possible_countries["Team"]:
            temp = 0
            if (i == self.playernick):
                resultFyle = open("datasets/country.csv", 'w')
                for r in RESULTS:
                    resultFyle.write(r + "\n")
                resultFyle.close()
                temp = 1
                messagebox.showinfo("Info", "Great, we got your country!")
                break
        if(temp == 0):
            messagebox.showerror("Error", "Please, enter your country correctly!!!")


    def choose1(self,event):
        nicknamepath = Path('datasets/country.csv')
        checkerpath = Path('datasets/check_if_filled_in.csv')
        if (nicknamepath.exists()==0 or checkerpath.exists()==0):
            messagebox.showerror("Error", "Please, enter your country and Fill in doc!!!")
        else:
            self.quit()
            os.system('python wp_core.py')


if __name__ == '__main__':
    start = Controller()
    start.run()
