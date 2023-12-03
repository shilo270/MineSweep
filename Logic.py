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
        self.label = tk.Label(text="MineSweep", height=2, bg="lightgray", bd=5, fg="black", font=("Courier", 44))
        self.label.pack(pady=0)
        self.label.place(x=200, y=10)
        #self.root.attributes('-fullscreen',True)
        self.GridSize = 15
        self.init_game()
        self.resetButton = tk.Button(root, text="Restart game",command=self.restartGame, height=1, width=18, bd='5', font=("Ariel", 10))
        self.resetButton.pack(pady=0,padx=0)
        self.resetButton.place(x=10, y=155)
        self.amountOfTiles = self.GridSize * self.GridSize
        self.amount_of_tiles_with_numbers = self.amountOfTiles - self.amount_of_bombs
        self.currnt_number_bombs = tk.Label(root, text="number of bombs: " + str(self.currntNumberOfBombs), height=1, width=18, bd='5', font=("Ariel", 10))
        self.currnt_number_bombs.pack(pady=0,padx=0)
        self.currnt_number_bombs.place(x=10, y=200)


    def init_game(self):
        self.list_Of_Tiles = [[] for self.GridSize in range(self.GridSize + 1)]
        del self.list_Of_Tiles[-1]
        self.flagNumber = 0
        self.amount_of_bombs = 40
        self.amount_of_tiles_with_numbers_revealed = 0
        self.currntNumberOfBombs = self.amount_of_bombs
        self.label.configure(text="MineSweep")




        #create buttons + title
        for i in range(self.GridSize):
            for j in range(self.GridSize):
                myButton = Button(root)
                myButton.button.place(x=(j+1)*24 + 150, y=(i+1)*25+ 130)
                self.list_Of_Tiles[i].append(myButton)
                myButton.index = (i , j)
                length = len(self.list_Of_Tiles) - 1
                # TopLeftCorner
                if i == 0 and j == 0:
                    myButton.tileSide = 1
                # topRow without corners
                elif i == 0 and j != 0 and j !=length:
                    myButton.tileSide = 2
                # TopRightCorner
                elif i == 0 and j == length:
                    myButton.tileSide = 3
                # left Column without corners
                elif j == 0 and i != 0 and i != length:
                    myButton.tileSide = 4
                # myButton.tileSide = 5 ---> mid tiles set as default
                # right column without corners
                elif j == length and i != 0 and i != length:
                    myButton.tileSide = 6
                # BotLeftCorner
                elif i == length and j == 0:
                    myButton.tileSide = 7
                # bottom row without corners
                elif i == length and j != 0 and j != length:
                    myButton.tileSide = 8
                # BotRightCorner
                elif i == length and j == length:
                    myButton.tileSide = 9


        self.placeMines(self.amount_of_bombs)


    def right_click(self, event):
        self.button.configure(image=self.MineImage, height=20, width=18, bg="red")


    def restartGame(self):
        self.flagNumber = 0
        self.amount_of_bombs = 40
        self.amount_of_tiles_with_numbers_revealed = 0
        for row in self.list_Of_Tiles:
            for b in row:
                b.resetButton()

        self.placeMines(self.amount_of_bombs)
        self.currntNumberOfBombs = self.amount_of_bombs
        self.currnt_number_bombs.configure(text="number of bombs: " + str(self.currntNumberOfBombs))
        pass

    def win_condition(self):
        if self.amount_of_tiles_with_numbers_revealed == self.amount_of_tiles_with_numbers:
            myMsg = "you win!"
            self.label.configure(myMsg)
            self.endGame()
    def endGame(self):
        for i in range(len(self.list_Of_Tiles)):
            for j in range(len(self.list_Of_Tiles[0])):
                b = self.list_Of_Tiles[i][j]
                b.button.configure(command=self.do_nothing)
                if b.placedMine == True:
                    b.button.configure(image=b.MineImage, height=20, width=18)
                b.button.unbind('<Button-3>')


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
            self.list_Of_Tiles[x][y].numberOnTile = -1
            i += 1

        for i in range(len(self.list_Of_Tiles)):
            for j in range(len(self.list_Of_Tiles[0])):
                #checks if thers is a bombs on the tile
                if self.list_Of_Tiles[i][j].placedMine == True:
                    continue
                countBombs = 0
                match self.list_Of_Tiles[i][j].tileSide:
                    case 1:
                        if self.list_Of_Tiles[i][j + 1].placedMine == True:
                            countBombs += 1
                        if self.list_Of_Tiles[i + 1][j + 1].placedMine == True:
                            countBombs += 1
                        if self.list_Of_Tiles[i + 1][j].placedMine == True:
                            countBombs += 1
                    case 2:
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

                    case 3:
                        if self.list_Of_Tiles[i + 1][j].placedMine == True:
                            countBombs += 1
                        if self.list_Of_Tiles[i + 1][j - 1].placedMine == True:
                            countBombs += 1
                        if self.list_Of_Tiles[i][j - 1].placedMine == True:
                            countBombs += 1
                    case 4:
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
                    case 5:
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
                    case 6:
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
                    case 7:
                        if self.list_Of_Tiles[i][j + 1].placedMine == True:
                            countBombs += 1
                        if self.list_Of_Tiles[i - 1][j].placedMine == True:
                            countBombs += 1
                        if self.list_Of_Tiles[i - 1][j + 1].placedMine == True:
                            countBombs += 1
                    case 8:
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
                    case 9:
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
        self.placedMine = False
        self.MineImage =ImageTk.PhotoImage(Image.open('MineImage.png').resize((13,13)))
        self.FlagImage =ImageTk.PhotoImage(Image.open('Flag.png').resize((13,13)))
        self.TransparentImage =ImageTk.PhotoImage(Image.open('transparent.png').resize((13,13)))
        self.button = tk.Button(root, command=self.pressedButton,height=1, width=2)
        self.defaultColor = self.button.cget('bg')
        self.placedNumber = False
        self.numberOnTile = 0
        self.index = (0,0)
        # 5 = mid tiles
        self.tileSide = 5
        self.button.bind('<Button-3>', self.pressedRight)
        self.flag = False
    #def openAdjacentTiles(pressedButton(self)):
    def resetButton(self):
        self.button.configure(text = "",image="",command=self.pressedButton, height=1, width=2,background=self.defaultColor)
        self.placedMine = False
        self.placedNumber = False
        self.numberOnTile = 0
        self.flag = False
        self.button.bind('<Button-3>', self.pressedRight)
    def pressedRight(self, event):
        if self.flag == False:
            if self.placedNumber == True:
                pass
            else:
                self.button.configure(image=self.FlagImage, height=20, width=18)
                window.flagNumber += 1
                self.flag = True
                window.currntNumberOfBombs -= 1
                window.currnt_number_bombs.configure(text="number of bombs: " +  str(window.currntNumberOfBombs))
        else:
            self.button.configure(image="", height=1, width=2)
            self.flag = False
            window.currntNumberOfBombs += 1
            window.currnt_number_bombs.configure(text="number of bombs: " +  str(window.currntNumberOfBombs))

    def pressedButton(self, currentButton = None):

        msg = tk.Label(root, text="", height=2, bg="lightgray", bd=5, fg="black", font=("Courier", 44))
        msg.pack(pady=0)
        msg.place(x=90, y=13)
        if currentButton == None:

            if self.placedMine is True:
                window.label.configure(text ="You lost, game over")
                self.button.configure(image=self.MineImage,height=20, width=18,bg="red")
                window.endGame()

            else:
                if self.flag == True:
                    self.button.configure(text=self.numberOnTile,image="", height=1, width=2, font='sans 9 bold')
                else:
                    self.button.configure(text=self.numberOnTile, height=1, width=2, font='sans 9 bold')
                self.placedNumber = True
                window.amount_of_tiles_with_numbers_revealed += 1
                msg.configure(text="")
                window.win_condition()
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
            # if 0 press the adjacent tiles

        else:
            if currentButton.placedNumber == True:
                return
            if currentButton.flag == True:
                currentButton.button.configure(text=currentButton.numberOnTile, image="", height=1, width=2, font='sans 9 bold')
            else:
                currentButton.button.configure(text=currentButton.numberOnTile, height=1, width=2, font='sans 9 bold')
            currentButton.placedNumber = True
            window.amount_of_tiles_with_numbers_revealed += 1
            window.label.configure(text="")
            window.win_condition()
            match currentButton.numberOnTile:
                case 0:
                    currentButton.button.configure(fg="blue")
                case 1:
                    currentButton.button.configure(fg="green")
                case 2:
                    currentButton.button.configure(fg="orange")
                case 3:
                    currentButton.button.configure(fg="red")
                case 4:
                    currentButton.button.configure(fg="purple")
                case 5:
                    currentButton.button.configure(fg="brown")
                case 6:
                    currentButton.button.configure(fg="pink")
                case 7:
                    currentButton.button.configure(fg="cyan")
                case 8:
                    currentButton.button.configure(fg="black")
        if currentButton == None:

            if self.numberOnTile == 0:
                i = self.index[0]
                j = self.index[1]
                match self.tileSide:
                    case 1:
                        self.pressedButton(window.list_Of_Tiles[i + 1][j + 1])
                        self.pressedButton(window.list_Of_Tiles[i][j + 1])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j])
                    case 2:
                        self.pressedButton(window.list_Of_Tiles[i][j + 1])
                        self.pressedButton(window.list_Of_Tiles[i][j - 1])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j + 1])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j - 1])
                    case 3:
                        self.pressedButton(window.list_Of_Tiles[i][j - 1])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j - 1])
                    case 4:
                        self.pressedButton(window.list_Of_Tiles[i][j + 1])
                        self.pressedButton(window.list_Of_Tiles[i - 1][j])
                        self.pressedButton(window.list_Of_Tiles[i - 1][j + 1])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j + 1])
                    case 5:
                        self.pressedButton(window.list_Of_Tiles[i][j + 1])
                        self.pressedButton(window.list_Of_Tiles[i][j - 1])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j + 1])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j - 1])
                        self.pressedButton(window.list_Of_Tiles[i - 1][j + 1])
                        self.pressedButton(window.list_Of_Tiles[i - 1][j])
                        self.pressedButton(window.list_Of_Tiles[i - 1][j - 1])
                    case 6:
                        self.pressedButton(window.list_Of_Tiles[i][j - 1])
                        self.pressedButton(window.list_Of_Tiles[i - 1][j])
                        self.pressedButton(window.list_Of_Tiles[i - 1][j - 1])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j - 1])
                    case 7:
                        self.pressedButton(window.list_Of_Tiles[i][j + 1])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j + 1])
                        self.pressedButton(window.list_Of_Tiles[i + 1][j])
                    case 8:
                        self.pressedButton(window.list_Of_Tiles[i][j - 1])
                        self.pressedButton(window.list_Of_Tiles[i][j + 1])
                        self.pressedButton(window.list_Of_Tiles[i - 1][j - 1])
                        self.pressedButton(window.list_Of_Tiles[i - 1][j])
                        self.pressedButton(window.list_Of_Tiles[i - 1][j + 1])
                    case 9:
                        self.pressedButton(window.list_Of_Tiles[i][j - 1])
                        self.pressedButton(window.list_Of_Tiles[i - 1][j - 1])
                        self.pressedButton(window.list_Of_Tiles[i - 1][j])
        else:
            if currentButton.numberOnTile == 0:
                i = currentButton.index[0]
                j = currentButton.index[1]
                match currentButton.tileSide:
                    case 1:
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j + 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i][j + 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j])
                    case 2:
                        currentButton.pressedButton(window.list_Of_Tiles[i][j + 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i][j - 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j + 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j])
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j - 1])
                    case 3:
                        currentButton.pressedButton(window.list_Of_Tiles[i][j - 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j])
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j - 1])
                    case 4:
                        currentButton.pressedButton(window.list_Of_Tiles[i][j + 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j + 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j])
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j + 1])
                    case 5:
                        currentButton.pressedButton(window.list_Of_Tiles[i][j + 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i][j - 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j + 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j])
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j - 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j + 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j - 1])
                    case 6:
                        currentButton.pressedButton(window.list_Of_Tiles[i][j - 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j - 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j])
                        currentButton.pressedButton(window.list_Of_Tiles[i + 1][j - 1])
                    case 7:
                        currentButton.pressedButton(window.list_Of_Tiles[i][j + 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j + 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j])
                    case 8:
                        currentButton.pressedButton(window.list_Of_Tiles[i][j - 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i][j + 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j - 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j + 1])
                    case 9:
                        currentButton.pressedButton(window.list_Of_Tiles[i][j - 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j - 1])
                        currentButton.pressedButton(window.list_Of_Tiles[i - 1][j])

root = tk.Tk()
window = Window(root)
root.mainloop()