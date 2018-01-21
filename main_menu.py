import tkinter as Tk
from tkinter import messagebox
import sys
import os

# class Model():
#     def __init__(self):


class View():
    def __init__(self, master):

        self.frame = Tk.Frame(master)
        self.logo = Tk.PhotoImage(file='media/logo.png')
        self.logo_label = Tk.Label(master, image=self.logo)
        self.logo_label.pack(side='top')
        self.about_app = Tk.Button(self.frame, text="About app",padx=5, pady=5)
        self.start_app = Tk.Button(self.frame, text="Start",padx=5, pady=5)
        self.about_authors_app = Tk.Button(self.frame, text="About authors",padx=5, pady=5)
        self.about_app.pack(side="top",fill=Tk.BOTH,padx=5, pady=5)
        self.start_app.pack(side="top",fill=Tk.BOTH,padx=5, pady=5)
        self.about_authors_app.pack(side="top",fill=Tk.BOTH,padx=5, pady=5)
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)



class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.root.resizable(False, False)
        # self.model = Model()
        self.root.eval('tk::PlaceWindow %s center' % self.root.winfo_pathname(self.root.winfo_id()))
        self.view = View(self.root)
        self.view.about_app.bind("<Button>",self.choose1)
        self.view.start_app.bind("<Button>",self.choose2)
        self.view.about_authors_app.bind("<Button>",self.choose3)

    def run(self):
        self.root.title("Score miner")
        self.root.deiconify()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

    def choose1(self,event):
        messagebox.showinfo("About App", "Score miner is an app dedicated to predict results of World Cup 2018"
                                         " and Bundesliga season 2017/2018. Hope you enjoy! More info -> README :)")

    def choose2(self,event):
        self.quit()
        os.system('python hub.py')

    def choose3(self,event):
        messagebox.showinfo("About Authors", "Michał Woźniak & Michał Wrzesiński")

if __name__ == '__main__':
    start = Controller()
    start.run()
