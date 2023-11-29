import time
import tkinter as tk
from PIL import Image,ImageTk
import random

class Window:
    def __init__(self,root):
        self.root = root
        self.root.title("MineSweep game")
        self.root.geometry("480x640")
        self.root.configure(bg="lightgray")
        #self.root.attributes('-fullscreen',True)
        self.GridSize = 5
        self.list_Of_Mines = [[] for self.GridSize in range(self.GridSize)]
        #self.canvas = Canvas(bg="pink", height="200")
        for i in range(self.GridSize):
            for j in range(self.GridSize):
                button = Button(root)
                button.button.place(x=(j+1)*24 - 13, y=(i+1)*25+ 130)
                self.list_Of_Mines[i].append(button)
        self.label = tk.Label(text="MineSweep", height=2, bg="lightgray",bd=5, fg="black", font=("Courier",44))
        self.label.pack(pady=0)
        self.label.place(x=90, y=10)
        self.placeMines(5)


    def placeMines(self,numberOfMines):
        listPlacedMines = []
        i = 0
        while i <= numberOfMines:
            x = random.randint(0, self.GridSize - 1)
            y = random.randint(0, self.GridSize - 1)
            if (x,y) in listPlacedMines:
                continue
            listPlacedMines.append((x, y))
            self.list_Of_Mines[x][y].placedMine = True
            i += 1
    # easy 9x9 number of mines 10
    # intermediate 16x16 number of mines 40
    # expert 16x30 number of mines 99
    # custom i x j number of mines k

class Button:
    def __init__(self,root):
        self.root = root
        self.button = tk.Button(root,command=self.pressedButton,height=1, width=2)
        self.placedMine = False
        self.MineImage =ImageTk.PhotoImage(Image.open('pngwing.png').resize((13,13)))


    def pressedButton(self):
        msg = tk.Label(root, text="", height=2, bg="lightgray", bd=5, fg="black", font=("Courier", 44))
        msg.pack(pady=0)
        msg.place(x=90, y=13)
        if self.placedMine is True:
            msg.configure(text ="You lost, game over")
            self.button.configure(image=self.MineImage,height=20, width=18,bg="red")
            # game over need work
        else:
            msg.configure(text="keep playing your good")
            for i in range(9):
                
            self.button.configure(text="3",height=1, width=2)


root = tk.Tk()
window = Window(root)
root.mainloop()