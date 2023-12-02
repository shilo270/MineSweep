import time
import tkinter as tk
from PIL import Image,ImageTk
import random

class Window:
    def __init__(self,root):
        self.root = root
        self.root.title("MineSweep game")
        self.root.geometry("900x900")
        self.root.configure(bg="lightgray")
        #self.root.attributes('-fullscreen',True)
        self.GridSize = 5
        self.list_Of_Tiles = [[] for self.GridSize in range(self.GridSize + 1)]
        del self.list_Of_Tiles[-1]
        self.resetButton = tk.Button(root, text="Restart game", height=1, width=12, bd='5', font=("Ariel", 15))
        self.resetButton.pack(pady=0,padx=0)
        self.resetButton.place(x=10, y=155)

        #create buttons + title
        for i in range(self.GridSize):
            for j in range(self.GridSize):
                button = Button(root)
                button.button.place(x=(j+1)*24 + 150, y=(i+1)*25+ 130)
                self.list_Of_Tiles[i].append(button)
                button.index = (i , j)
        self.label = tk.Label(text="MineSweep", height=2, bg="lightgray",bd=5, fg="black", font=("Courier",44))
        self.label.pack(pady=0)
        self.label.place(x=200, y=10)
        self.placeMines(5)

    def right_click(self, event):
        self.button.configure(image=self.MineImage, height=20, width=18, bg="red")



    # def resetGame(self):
    #     self.list_Of_Tiles = [[] for self.GridSize in range(self.GridSize + 1)]
    #     del self.list_Of_Tiles[-1]
    #     self.placeMines(5)
    #     for i in range(len(self.list_Of_Tiles)):
    #         for j in range(len(self.list_Of_Tiles[0])):
    #             Button.placedMine = False
    #     Button.msg.destroy
    #     pass

    def placeMines(self,numberOfMines):
        listPlacedMines = [0]
        i = 0
        while i < numberOfMines:
            x = random.randint(0, self.GridSize - 1)
            y = random.randint(0, self.GridSize - 1)
            if (x, y) in listPlacedMines:
                continue
            listPlacedMines.append((x, y))
            self.list_Of_Tiles[x][y].placedMine = True
            i += 1


        for i in range(len(self.list_Of_Tiles)):
            for j in range(len(self.list_Of_Tiles[0])):
                #checks if thers is a bombs on the tile
                if self.list_Of_Tiles[i][j].placedMine == True:
                    continue
                countBombs = 0
                # checks the center
                if i != 0 and i != len(self.list_Of_Tiles[0]) - 1:
                    if j != 0 and j != len(self.list_Of_Tiles[0]) - 1:
                        if self.list_Of_Tiles[i][j - 1].placedMine == True:
                            countBombs += 1
                        if self.list_Of_Tiles[i][j + 1].placedMine == True:
                            countBombs += 1
                        if self.list_Of_Tiles[i - 1][j - 1].placedMine == True:
                            countBombs += 1
                        if self.list_Of_Tiles[i - 1][j + 1].placedMine == True:
                            countBombs += 1
                        if self.list_Of_Tiles[i - 1][j].placedMine == True:
                            countBombs += 1
                        if self.list_Of_Tiles[i + 1][j - 1].placedMine == True:
                            countBombs += 1
                        if self.list_Of_Tiles[i + 1][j + 1].placedMine == True:
                            countBombs += 1
                        if self.list_Of_Tiles[i + 1][j].placedMine == True:
                            countBombs += 1
                        self.list_Of_Tiles[i][j].numberOnTile = countBombs
                #cheks the left column without corners
                if i !=0 and i != len(self.list_Of_Tiles[0])-1 and j == 0:
                    if self.list_Of_Tiles[i + 1][j].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i + 1][j + 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i][j + 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i - 1][j + 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i - 1][j].placedMine == True:
                        countBombs += 1

                #checks the right column without corners
                if i != 0 and i != len(self.list_Of_Tiles[0]) - 1 and j == len(self.list_Of_Tiles[0])-1:
                    if self.list_Of_Tiles[i + 1][j].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i + 1][j - 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i][j - 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i - 1][j - 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i - 1][j].placedMine == True:
                        countBombs += 1

                #checks the top row without corners
                if i == 0 and j != len(self.list_Of_Tiles[0])-1 and j != 0:
                    if self.list_Of_Tiles[i][j + 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i + 1][j + 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i + 1][j].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i][j - 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i + 1][j - 1].placedMine == True:
                        countBombs += 1
                #checks the bottom row without corners
                if i == len(self.list_Of_Tiles[0])-1 and j != len(self.list_Of_Tiles[0])-1 and j != 0:
                    if self.list_Of_Tiles[i][j + 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i - 1][j + 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i - 1][j].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i][j - 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i - 1][j - 1].placedMine == True:
                        countBombs += 1
                #check all corners
                if i == 0 and j == 0:
                    if self.list_Of_Tiles[i][j + 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i + 1][j + 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i + 1][j].placedMine == True:
                        countBombs += 1
                if i == 0 and j == len(self.list_Of_Tiles) - 1:
                    if self.list_Of_Tiles[i + 1][j].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i + 1][j - 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i][j - 1].placedMine == True:
                        countBombs += 1
                if i == len(self.list_Of_Tiles) - 1 and j == 0:
                    if self.list_Of_Tiles[i][j + 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i - 1][j].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i - 1][j + 1].placedMine == True:
                        countBombs += 1
                if i == len(self.list_Of_Tiles) - 1 and j == i == len(self.list_Of_Tiles) - 1:
                    if self.list_Of_Tiles[i - 1][j - 1].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i - 1][j].placedMine == True:
                        countBombs += 1
                    if self.list_Of_Tiles[i][j - 1].placedMine == True:
                        countBombs += 1
                self.list_Of_Tiles[i][j].numberOnTile = countBombs

    def do_nothing(self):
        pass
    # easy 9x9 number of mines 10
    # intermediate 16x16 number of mines 40
    # expert 16x30 number of mines 99
    # custom i x j number of mines k

class Button:
    def __init__(self,root):
        self.root = root
        self.button = tk.Button(root,command=self.pressedButton,height=1, width=2)
        self.placedMine = False
        self.MineImage =ImageTk.PhotoImage(Image.open('MineImage.png').resize((13,13)))
        self.numberOnTile = 0
        self.index = (0,0)

    #def openAdjacentTiles(pressedButton(self)):



    def pressedButton(self):
        msg = tk.Label(root, text="", height=2, bg="lightgray", bd=5, fg="black", font=("Courier", 44))
        msg.pack(pady=0)
        msg.place(x=90, y=13)
        if self.placedMine is True:
            msg.configure(text ="You lost, game over")
            self.button.configure(image=self.MineImage,height=20, width=18,bg="red")
            for i in range(len(window.list_Of_Tiles)):
                for j in range(len(window.list_Of_Tiles[0])):
                    window.list_Of_Tiles[i][j].button.configure(command=window.do_nothing)
                    if window.list_Of_Tiles[i][j].placedMine == True:
                        window.list_Of_Tiles[i][j].button.configure(image=self.MineImage,height=20, width=18)


        else:
            msg.configure(text="keep playing your good")
            self.button.configure(text=self.numberOnTile, height=1, width=2, font='sans 9 bold')
            match self.numberOnTile:
                case 0:
                    self.button.configure(fg="blue")
                case 1:
                    self.button.configure(fg="green")
                case 2:
                    self.button.configure(fg="orange")
                case 3:
                    self.button.configure(fg="red")
                case 4:
                    self.button.configure(fg="purple")
                case 5:
                    self.button.configure(fg="brown")
                case 6:
                    self.button.configure(fg="pink")
                case 7:
                    self.button.configure(fg="cyan")
                case 8:
                    self.button.configure(fg="black")
            if self.numberOnTile == 0:
                i = self.index[0]
                j = self.index[1]

root = tk.Tk()
window = Window(root)
root.mainloop()