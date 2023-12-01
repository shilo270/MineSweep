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
        self.list_Of_Tiles = [[] for self.GridSize in range(self.GridSize)]
        for i in range(self.GridSize):
            for j in range(self.GridSize):
                button = Button(root)
                button.button.place(x=(j+1)*24 - 13, y=(i+1)*25+ 130)
                self.list_Of_Tiles[i].append(button)
        self.label = tk.Label(text="MineSweep", height=2, bg="lightgray",bd=5, fg="black", font=("Courier",44))
        self.label.pack(pady=0)
        self.label.place(x=90, y=10)
        self.placeMines(5)


    def do_nothing(self):
        pass


    def placeMines(self,numberOfMines):
        self.listPlacedMines = []
        i = 0
        while i <= numberOfMines:
            x = random.randint(0, self.GridSize - 1)
            y = random.randint(0, self.GridSize - 1)
            if (x,y) in self.listPlacedMines:
                continue
            self.listPlacedMines.append((x, y))
            self.list_Of_Tiles[x][y].placedMine = True
            i += 1
    # easy 9x9 number of mines 10
    # intermediate 16x16 number of mines 40
    # expert 16x30 number of mines 99
    # custom i x j number of mines k

class Button:
    def __init__(self,root):
        self.root = root
        self.button = tk.Button(root, command=self.pressedButtonLeft, height=1, width=2)
        self.placedMine = False
        self.MineImage =ImageTk.PhotoImage(Image.open('MineImage.png').resize((13,13)))
        self.FlagImage =ImageTk.PhotoImage(Image.open('Flag.png').resize((13,13)))
        self.root.bind('<Button-1>', pressedButtonLeft)
        self.root.bind('<Button-3>', pressedButtonRight)


    def pressedButtonRight(self):
        self.button.configure(image=self.FlagImage, height=20, width=18)

    def pressedButtonLeft(self):
        msg = tk.Label(root, text="", height=2, bg="lightgray", bd=5, fg="black", font=("Courier", 44))
        msg.pack(pady=0)
        msg.place(x=90, y=13)
        if self.placedMine is True:
            msg.configure(text ="You lost, game over")
            for i in window.listPlacedMines:
                self.button = self.list_Of_Tiles[i[0]][i[1]]
                self.button.configure(image=self.MineImage,height=20, width=18,bg="red")
            self.button.configure(image=self.MineImage,height=20, width=18,bg="red")
        for r in self.list_Of_Tiles:
            for b in r:
                b.button.configure(command=window.do_nothing)
            # game over need work
        else:
            msg.configure(text="keep playing your good")
            index = window.list_Of_Tiles.index(self)
            print(index)
            adjacencyMines = 0
            if window.list_Of_Tiles[index - 1][index - 1].placedMine == True:
                adjacencyMines += 1
            if window.list_Of_Tiles[index][index - 1].placedMine == True:
                adjacencyMines += 1
            if window.list_Of_Tiles[index + 1][index - 1].placedMine == True:
                adjacencyMines += 1
            if window.list_Of_Tiles[index - 1][index].placedMine == True:
                adjacencyMines += 1
            if window.list_Of_Tiles[index - 1][index + 1].placedMine == True:
                adjacencyMines += 1
            if window.list_Of_Tiles[index][index + 1].placedMine == True:
                adjacencyMines += 1
            if window.list_Of_Tiles[index + 1][index + 1].placedMine == True:
                adjacencyMines += 1
            if window.list_Of_Tiles[index + 1][index].placedMine == True:
                adjacencyMines += 1

            match adjacencyMines:
                case 0:
                    self.button.configure(text="", fg='blue', height=1, width=2)
                case 1:
                    self.button.configure(text="adjacencyMines",fg='blue', height=1, width=2)
                case 2:
                    self.button.configure(text="adjacencyMines", fg='red', height=1, width=2)
                case 3:
                    self.button.configure(text="adjacencyMines", fg='green', height=1, width=2)
                case 4:
                    self.button.configure(text="adjacencyMines", fg='yellow', height=1, width=2)
                case 5:
                    self.button.configure(text="adjacencyMines", fg='brown', height=1, width=2)
                case 6:
                    self.button.configure(text="adjacencyMines", fg='purple', height=1, width=2)
                case 7:
                    self.button.configure(text="adjacencyMines", fg='orange', height=1, width=2)
                case 8:
                    self.button.configure(text="adjacencyMines", fg='black', height=1, width=2)
            self.button.configure(text="adjacencyMines",height=1, width=2)


root = tk.Tk()
window = Window(root)
root.mainloop()