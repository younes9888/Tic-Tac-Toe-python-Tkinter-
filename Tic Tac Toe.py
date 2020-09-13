from random import randint
from tkinter import *
from tkinter import ttk, messagebox
import sys
import os

class tictactoe():
    Activeplayer = randint(1,2)
    player1 = []
    player2 = []
    clicknumber = 9
    def __init__(self, parent):
        #ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_window()
    def BuClick(self,id):

        if (self.Activeplayer==1):
            self.SetLayout(id,"X")
            self.player1.append(id)
            self.verfywinner()
            self.clicknumber=self.clicknumber-1
            if self.clicknumber==0:
                self.educeasking()
            self.parent.title("Tic Tac Toe Player 2")
            self.Activeplayer=2
        elif (self.Activeplayer==2):
            self.SetLayout(id,"O")
            self.player2.append(id)
            self.verfywinner()
            self.clicknumber=self.clicknumber-1
            if self.clicknumber==0:
                self.educeasking()
            self.parent.title("Tic Tac Toe Player 1")
            self.Activeplayer=1
    def SetLayout(self,id,text):
        if (id == 1 ):
            self.but1.config(text=text)
            self.but1.state(['disabled'])
        elif (id == 2):
            self.but2.config(text=text)
            self.but2.state(['disabled'])
        elif (id == 3):
            self.but3.config(text=text)
            self.but3.state(['disabled'])
        elif (id == 4):
            self.but4.config(text=text)
            self.but4.state(['disabled'])
        elif (id == 5):
            self.but5.config(text=text)
            self. but5.state(['disabled'])
        elif (id == 6):
            self.but6.config(text=text)
            self.but6.state(['disabled'])
        elif (id == 7):
            self.but7.config(text=text)
            self.but7.state(['disabled'])
        elif (id == 8):
            self.but8.config(text=text)
            self.but8.state(['disabled'])
        elif (id == 9):
            self.but9.config(text=text)
            self.but9.state(['disabled'])

    def verfywinner(self):
        if   (1 in self.player1 and 2 in self.player1 and 3 in self.player1 or 4 in self.player1 and 5 in self.player1 and 6 in self.player1 or 7 in self.player1 and 8 in self.player1 and 9 in self.player1 or 1 in self.player1 and 4 in self.player1 and 7 in self.player1 or 2 in self.player1 and 5 in self.player1 and 8 in self.player1 or 3 in self.player1 and 6 in self.player1 and 9 in self.player1):
            p=1
            self.asking(p)

        elif (1 in self.player2 and 2 in self.player2 and 3 in self.player2 or 4 in self.player2 and 5 in self.player2 and 6 in self.player2 or 7 in self.player2 and 8 in self.player2 and 9 in self.player2 or 1 in self.player2 and 4 in self.player2 and 7 in self.player2 or 2 in self.player2 and 5 in self.player2 and 8 in self.player2 or 3 in self.player2 and 6 in self.player2 and 9 in self.player2):
            p = 2
            self.asking(p)

    def asking(self,p):
        msgbox = messagebox.askquestion(title='Tic Tac Toe', message='Player'+' '+str(p)+' '+ 'is the winner\n Do you want to replay?', icon='info')
        if msgbox == 'no':
            self.parent.destroy()
        else:
            self.player1.clear()
            self.player2.clear()
            self.parent.destroy()
            startgame()
    def educeasking(self):
        msgbox = messagebox.askquestion(title='Tic Tac Toe', message='Draw'+'\n Do you want to replay?', icon='info')
        if msgbox == 'no':
            self.parent.destroy()
        else:
            self.player1.clear()
            self.player2.clear()
            self.parent.destroy()
            startgame()

    def initialize_window(self):
        self.parent.title("Tic Tac Toe Player 1")
        self.style = ttk.Style()
        self.style.theme_use('classic')
        self.but1 = ttk.Button(self.parent, text='')
        self.but1.grid(row=0, column=0, sticky='snew', ipadx=50, ipady=50)
        self.but1.config(command=lambda : self.BuClick(1))
        self.but2 = ttk.Button(self.parent, text='')
        self.but2.grid(row=0, column=1, sticky='snew', ipadx=50, ipady=50)
        self.but2.config(command=lambda : self.BuClick(2))
        self.but3 = ttk.Button(self.parent, text='')
        self.but3.grid(row=0, column=2, sticky='snew', ipadx=50, ipady=50)
        self.but3.config(command=lambda : self.BuClick(3))
        self.but4 = ttk.Button(self.parent, text='')
        self.but4.grid(row=1, column=0, sticky='snew', ipadx=50, ipady=50)
        self.but4.config(command=lambda : self.BuClick(4))
        self.but5 = ttk.Button(self.parent, text='')
        self.but5.grid(row=1, column=1, sticky='snew', ipadx=50, ipady=50)
        self.but5.config(command=lambda : self.BuClick(5))
        self.but6 = ttk.Button(self.parent, text='')
        self.but6.grid(row=1, column=2, sticky='snew', ipadx=50, ipady=50)
        self.but6.config(command=lambda : self.BuClick(6))
        self.but7 = ttk.Button(self.parent, text='')
        self.but7.grid(row=2, column=0, sticky='snew', ipadx=50, ipady=50)
        self.but7.config(command=lambda : self.BuClick(7))
        self.but8 = ttk.Button(self.parent, text='')
        self.but8.grid(row=2, column=1, sticky='snew', ipadx=50, ipady=50)
        self.but8.config(command=lambda : self.BuClick(8))
        self.but9 = ttk.Button(self.parent, text='')
        self.but9.grid(row=2, column=2, sticky='snew', ipadx=50, ipady=50)
        self.but9.config(command=lambda : self.BuClick(9))
def startgame():
    global game
    if __name__ == '__main__':
       window = Tk()
       window.resizable(False, False)
       game = tictactoe(window)
       window.mainloop()
startgame()

