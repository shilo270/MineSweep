import time
import tkinter as tk
#from PIL import Image,ImageTk
import random

class Window:
    def __init__(self,root):
        self.root = root
        self.root.title("MineSweep game")
        self.root.geometry("480x640")
        self.root.configure(bg="lightgray")
        self.GridSize = 20
        self.numberOfMines = 20
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


    def placeMines(numberOfMines):
        ListPlacedMines = []
        i = 0
        while i <= numberOfMines:
            x = random.randint(0, window.numberOfMines)
            y = random.randint(0, window.numberOfMines)
            for j in range(len(ListPlacedMines)):
                if ListPlacedMines(j) == (x, y):
                    break
                if j == len(ListPlacedMines) and ListPlacedMines(j) != (x, y):
                    ListPlacedMines.append((x, y))
                    Button.self.list_Of_Mines[x][y].placedMine = True
                    print(ListPlacedMines)
                    i += 1
    # easy 9x9 number of mines 10
    # intermediate 16x16 number of mines 40
    # expert 16x30 number of mines 99
    # custom i x j number of mines k

class Button:
    def __init__(self,root):
        self.root = root
        self.button = tk.Button(root,height=1, width=2)
        self.placedMine = False

    def pressedButton(self):
        if Button.placedMine == True:
            Window.label = tk.Label(text="You lost, game over", height=2, bg="lightgray", bd=5, fg="black",
                                  font=("Courier", 44))
            Window.label.pack(pady=0)
            Window.label.place(x=90, y=13)
            # game over need work
        else:
            if Button.placedMine == False:
                


root = tk.Tk()
#Window.placeMines(10)
window = Window(root)
root.mainloop()