import tkinter as tk
from PIL import Image, ImageTk
import random


class Window:
    def __init__(self, root):
        self.root = root
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.window_width = 900
        self.window_height = 600
        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)
        self.root.title("MineSweep game")
        self.root.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')
        self.root.configure(bg="lightgray")

        self.label = tk.Label(text="MineSweep", height=2, bg="lightgray", bd=5, fg="black", font=("Courier", 44))
        self.label.pack(pady=0)
        self.label.place(x=200, y=10)
        #self.root.attributes('-fullscreen', True)
        self.GridSize = 5
        self.init_game()
        self.resetButton = tk.Button(root, text="Restart game", command=self.restart_game, height=1, width=18, bd='5', font=("Ariel", 10))
        self.resetButton.pack(pady=0, padx=0)
        self.resetButton.place(x=10, y=155)
        self.amountOfTiles = self.GridSize * self.GridSize
        self.amount_of_tiles_with_numbers = self.amountOfTiles - self.amount_of_bombs
        self.currnt_number_bombs = tk.Label(root, text="number of bombs: " + str(self.currntNumberOfBombs), height=1, width=18, bd='5', font=("Ariel", 10))
        self.currnt_number_bombs.pack(pady=0, padx=0)
        self.currnt_number_bombs.place(x=10, y=200)


        self.eazy_button = tk.Button(root, text="Easy", command=self.easy_mode, height=1, width=18, bd='5', font=("Ariel", 10))
        self.eazy_button.pack(pady=0, padx=0)
        self.eazy_button.place(x=10, y=250)

        self.hard_button = tk.Button(root, text="Hard", command=self.hard_mode, height=1, width=18, bd='5', font=("Ariel", 10))
        self.hard_button.pack(pady=0, padx=0)
        self.hard_button.place(x=10, y=300)

        self.insane_button = tk.Button(root, text="Insane", command=self.insane_mode, height=1, width=18, bd='5', font=("Ariel", 10))
        self.insane_button.pack(pady=0, padx=0)
        self.insane_button.place(x=10, y=350)

    def easy_mode(self):
        self.GridSize = 5
        self.amount_of_bombs = self.GridSize * self.GridSize/5
        self.amountOfTiles = self.GridSize * self.GridSize
        self.amount_of_tiles_with_numbers = self.amountOfTiles - self.amount_of_bombs
        for i in range(len(self.list_of_tiles)):
            for j in range(len(self.list_of_tiles[0])):
                self.list_of_tiles[i][j].button.destroy()
        self.list_of_tiles = [[] for self.GridSize in range(self.GridSize + 1)]
        del self.list_of_tiles[-1]
        self.create_buttons()
        self.restart_game(5)


    def hard_mode(self):
        self.GridSize = 15
        self.amount_of_bombs = self.GridSize * self.GridSize/5
        self.amountOfTiles = self.GridSize * self.GridSize
        self.amount_of_tiles_with_numbers = self.amountOfTiles - self.amount_of_bombs
        for i in range(len(self.list_of_tiles)):
            for j in range(len(self.list_of_tiles[0])):
                self.list_of_tiles[i][j].button.destroy()
        self.list_of_tiles = [[] for self.GridSize in range(self.GridSize + 1)]
        del self.list_of_tiles[-1]
        self.create_buttons()
        self.restart_game(50)
    def insane_mode(self):
        self.GridSize = 25
        self.amount_of_bombs = self.GridSize * self.GridSize/5
        self.amountOfTiles = self.GridSize * self.GridSize
        self.amount_of_tiles_with_numbers = self.amountOfTiles - self.amount_of_bombs
        for i in range(len(self.list_of_tiles)):
            for j in range(len(self.list_of_tiles[0])):
                self.list_of_tiles[i][j].button.destroy()
        self.list_of_tiles = [[] for self.GridSize in range(self.GridSize + 1)]
        del self.list_of_tiles[-1]
        self.create_buttons()
        self.restart_game(100)


    def init_game(self):
        self.list_of_tiles = [[] for self.GridSize in range(self.GridSize + 1)]
        del self.list_of_tiles[-1]
        self.flagNumber = 0
        self.amount_of_bombs = 5
        self.amount_of_tiles_with_numbers_revealed = 0
        self.currntNumberOfBombs = self.amount_of_bombs
        self.label.configure(text="MineSweep")
        self.create_buttons()

    def create_buttons(self):
        #create buttons + title
        for i in range(self.GridSize):
            for j in range(self.GridSize):
                myButton = Button(root)
                myButton.button.place(x=(j+1)*24 + 150, y=(i+1)*25 + 130)
                self.list_of_tiles[i].append(myButton)
                myButton.index = (i, j)
                length = len(self.list_of_tiles) - 1
                # TopLeftCorner
                if i == 0 and j == 0:
                    myButton.tileSide = 1
                # topRow without corners
                elif i == 0 and j != 0 and j != length:
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
        self.place_mines(self.amount_of_bombs)

    def right_click(self, event):
        self.button.configure(image=self.MineImage, height=20, width=18, bg="red")


    def restart_game(self, bombs_number = None):
        self.flagNumber = 0
        if bombs_number == None:
            self.amount_of_bombs = self.GridSize * self.GridSize / 5
        else:
            self.amount_of_bombs = bombs_number
        self.amount_of_tiles_with_numbers_revealed = 0
        for row in self.list_of_tiles:
            for b in row:
                b.resetButton()
        self.label.configure(text="MineSweep")
        self.place_mines(self.amount_of_bombs)
        self.currntNumberOfBombs = self.amount_of_bombs
        self.currnt_number_bombs.configure(text="number of bombs: " + str(self.currntNumberOfBombs))
        pass

    def win_condition(self):
        if self.amount_of_tiles_with_numbers_revealed == self.amount_of_tiles_with_numbers:
            my_msg = "you win!"
            self.label.configure(text=my_msg)
            self.end_game()

    def end_game(self):
        for i in range(len(self.list_of_tiles)):
            for j in range(len(self.list_of_tiles[0])):
                b = self.list_of_tiles[i][j]
                b.button.configure(command=self.do_nothing)
                if b.placedMine:
                    b.button.configure(image=b.MineImage, height=20, width=18)
                b.button.unbind('<Button-3>')

    def place_mines(self, number_of_mines):
        list_placed_mines = [0]
        i = 0
        while i < number_of_mines:
            x = random.randint(0, self.GridSize - 1)
            y = random.randint(0, self.GridSize - 1)
            if (x, y) in list_placed_mines:
                continue
            list_placed_mines.append((x, y))
            self.list_of_tiles[x][y].placedMine = True
            self.list_of_tiles[x][y].numberOnTile = -1
            i += 1

        for i in range(len(self.list_of_tiles)):
            for j in range(len(self.list_of_tiles[0])):
                #checks if thers is a bombs on the tile
                if self.list_of_tiles[i][j].placedMine:
                    continue
                count_bombs = 0
                match self.list_of_tiles[i][j].tileSide:
                    case 1:
                        if self.list_of_tiles[i][j + 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i + 1][j + 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i + 1][j].placedMine:
                            count_bombs += 1
                    case 2:
                        if self.list_of_tiles[i][j + 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i + 1][j + 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i + 1][j].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i][j - 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i + 1][j - 1].placedMine:
                            count_bombs += 1

                    case 3:
                        if self.list_of_tiles[i + 1][j].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i + 1][j - 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i][j - 1].placedMine:
                            count_bombs += 1
                    case 4:
                        if self.list_of_tiles[i + 1][j].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i + 1][j + 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i][j + 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i - 1][j + 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i - 1][j].placedMine:
                            count_bombs += 1
                    case 5:
                        if self.list_of_tiles[i][j - 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i][j + 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i - 1][j - 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i - 1][j + 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i - 1][j].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i + 1][j - 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i + 1][j + 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i + 1][j].placedMine:
                            count_bombs += 1
                    case 6:
                        if self.list_of_tiles[i + 1][j].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i + 1][j - 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i][j - 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i - 1][j - 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i - 1][j].placedMine:
                            count_bombs += 1
                    case 7:
                        if self.list_of_tiles[i][j + 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i - 1][j].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i - 1][j + 1].placedMine:
                            count_bombs += 1
                    case 8:
                        if self.list_of_tiles[i][j + 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i - 1][j + 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i - 1][j].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i][j - 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i - 1][j - 1].placedMine:
                            count_bombs += 1
                    case 9:
                        if self.list_of_tiles[i - 1][j - 1].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i - 1][j].placedMine:
                            count_bombs += 1
                        if self.list_of_tiles[i][j - 1].placedMine:
                            count_bombs += 1
                self.list_of_tiles[i][j].numberOnTile = count_bombs


    def do_nothing(self):
        pass
    # easy 9x9 number of mines 10
    # intermediate 16x16 number of mines 40
    # expert 16x30 number of mines 99
    # custom i x j number of mines k

class Button:
    def __init__(self, root):
        self.root = root
        self.placedMine = False
        self.MineImage = ImageTk.PhotoImage(Image.open('MineImage.png').resize((13, 13)))
        self.FlagImage = ImageTk.PhotoImage(Image.open('Flag.png').resize((13, 13)))
        self.TransparentImage = ImageTk.PhotoImage(Image.open('transparent.png').resize((13, 13)))
        self.button = tk.Button(root, command=self.pressedButton, height=1, width=2)
        self.defaultColor = self.button.cget('bg')
        self.placedNumber = False
        self.numberOnTile = 0
        self.index = (0, 0)
        self.adjacentFlags = 0
        # 5 = mid tiles
        self.tileSide = 5
        self.button.bind('<Button-3>', self.pressed_right)
        self.flag = False

    def resetButton(self):
        self.button.configure(text="", image="", command=self.pressedButton, height=1, width=2, background=self.defaultColor)
        self.placedMine = False
        self.placedNumber = False
        self.numberOnTile = 0
        self.flag = False
        self.button.bind('<Button-3>', self.pressed_right)
        self.adjacentFlags = 0

    def pressed_right(self, event):
        i = self.index[0]
        j = self.index[1]
        if not self.flag:
            if self.placedNumber:
                if self.adjacentFlags == self.numberOnTile:
                    self.adjacent_press(self, i, j)
                pass
            else:
                self.adjacent_add_flag(i, j, 1, True)
                self.button.configure(image=self.FlagImage, height=20, width=18)
                window.flagNumber += 1
                window.currntNumberOfBombs -= 1
                window.currnt_number_bombs.configure(text="number of bombs: " + str(window.currntNumberOfBombs))
        else:
            self.button.configure(image="", height=1, width=2)
            window.currntNumberOfBombs += 1
            window.currnt_number_bombs.configure(text="number of bombs: " + str(window.currntNumberOfBombs))
            self.adjacent_add_flag(i, j, -1, False)

    def pressedButton(self, current_button=None):
        if self.flag:
            return
        msg = tk.Label(root, text="", height=2, bg="lightgray", bd=5, fg="black", font=("Courier", 44))
        msg.pack(pady=0)
        msg.place(x=90, y=13)
        if current_button == None:
            if self.placedMine:
                window.label.configure(text ="You lost, game over")
                self.button.configure(image=self.MineImage,height=20, width=18,bg="red")
                window.end_game()
                return
            else:
                if self.flag:
                    self.button.configure(text=self.numberOnTile,image="", height=1, width=2, font='sans 9 bold')
                else:
                    self.button.configure(text=self.numberOnTile, height=1, width=2, font='sans 9 bold')
                self.placedNumber = True
                window.amount_of_tiles_with_numbers_revealed += 1
                msg.configure(text="")
                window.win_condition()
                self.text_colors(self)
        else:
            if current_button.flag:
                return
            if current_button.placedMine:
                window.label.configure(text ="You lost, game over")
                current_button.button.configure(image=current_button.MineImage, height=20, width=18, bg="red")
                window.end_game()
                return
            if current_button.placedNumber:
                return
            current_button.button.configure(text=current_button.numberOnTile, height=1, width=2, font='sans 9 bold')
            current_button.placedNumber = True
            window.amount_of_tiles_with_numbers_revealed += 1
            window.win_condition()
            self.text_colors(current_button)

        if current_button == None:
            if self.numberOnTile == 0:
                i = self.index[0]
                j = self.index[1]
                self.adjacent_press(self, i, j)
        else:
            if current_button.numberOnTile == 0:
                i = current_button.index[0]
                j = current_button.index[1]
                self.adjacent_press(current_button, i, j)

    def adjacent_press(self, current, i, j):
        match current.tileSide:
            case 1:
                current.pressedButton(window.list_of_tiles[i + 1][j + 1])
                current.pressedButton(window.list_of_tiles[i][j + 1])
                current.pressedButton(window.list_of_tiles[i + 1][j])
            case 2:
                current.pressedButton(window.list_of_tiles[i][j + 1])
                current.pressedButton(window.list_of_tiles[i][j - 1])
                current.pressedButton(window.list_of_tiles[i + 1][j + 1])
                current.pressedButton(window.list_of_tiles[i + 1][j])
                current.pressedButton(window.list_of_tiles[i + 1][j - 1])
            case 3:
                current.pressedButton(window.list_of_tiles[i][j - 1])
                current.pressedButton(window.list_of_tiles[i + 1][j])
                current.pressedButton(window.list_of_tiles[i + 1][j - 1])
            case 4:
                current.pressedButton(window.list_of_tiles[i][j + 1])
                current.pressedButton(window.list_of_tiles[i - 1][j])
                current.pressedButton(window.list_of_tiles[i - 1][j + 1])
                current.pressedButton(window.list_of_tiles[i + 1][j])
                current.pressedButton(window.list_of_tiles[i + 1][j + 1])
            case 5:
                current.pressedButton(window.list_of_tiles[i][j + 1])
                current.pressedButton(window.list_of_tiles[i][j - 1])
                current.pressedButton(window.list_of_tiles[i + 1][j + 1])
                current.pressedButton(window.list_of_tiles[i + 1][j])
                current.pressedButton(window.list_of_tiles[i + 1][j - 1])
                current.pressedButton(window.list_of_tiles[i - 1][j + 1])
                current.pressedButton(window.list_of_tiles[i - 1][j])
                current.pressedButton(window.list_of_tiles[i - 1][j - 1])
            case 6:
                current.pressedButton(window.list_of_tiles[i][j - 1])
                current.pressedButton(window.list_of_tiles[i - 1][j])
                current.pressedButton(window.list_of_tiles[i - 1][j - 1])
                current.pressedButton(window.list_of_tiles[i + 1][j])
                current.pressedButton(window.list_of_tiles[i + 1][j - 1])
            case 7:
                current.pressedButton(window.list_of_tiles[i][j + 1])
                current.pressedButton(window.list_of_tiles[i - 1][j + 1])
                current.pressedButton(window.list_of_tiles[i - 1][j])
            case 8:
                current.pressedButton(window.list_of_tiles[i][j - 1])
                current.pressedButton(window.list_of_tiles[i][j + 1])
                current.pressedButton(window.list_of_tiles[i - 1][j - 1])
                current.pressedButton(window.list_of_tiles[i - 1][j])
                current.pressedButton(window.list_of_tiles[i - 1][j + 1])
            case 9:
                current.pressedButton(window.list_of_tiles[i][j - 1])
                current.pressedButton(window.list_of_tiles[i - 1][j - 1])
                current.pressedButton(window.list_of_tiles[i - 1][j])

    def text_colors(self, current=None):
        match current.numberOnTile:
            case 0:
                current.button.configure(fg="blue")
            case 1:
                current.button.configure(fg="green")
            case 2:
                current.button.configure(fg="orange")
            case 3:
                current.button.configure(fg="red")
            case 4:
                current.button.configure(fg="purple")
            case 5:
                current.button.configure(fg="brown")
            case 6:
                current.button.configure(fg="pink")
            case 7:
                current.button.configure(fg="cyan")
            case 8:
                current.button.configure(fg="black")

    def adjacent_add_flag(self, i, j, to_add, TrueOrFalse):
        self.flag = TrueOrFalse
        match self.tileSide:
            case 1:
                window.list_of_tiles[i + 1][j + 1].adjacentFlags += to_add
                window.list_of_tiles[i][j + 1].adjacentFlags += to_add
                window.list_of_tiles[i + 1][j].adjacentFlags += to_add
            case 2:
                window.list_of_tiles[i][j + 1].adjacentFlags += to_add
                window.list_of_tiles[i][j - 1].adjacentFlags += to_add
                window.list_of_tiles[i + 1][j + 1].adjacentFlags += to_add
                window.list_of_tiles[i + 1][j].adjacentFlags += to_add
                window.list_of_tiles[i + 1][j - 1].adjacentFlags += to_add
            case 3:
                window.list_of_tiles[i][j - 1].adjacentFlags += to_add
                window.list_of_tiles[i + 1][j].adjacentFlags += to_add
                window.list_of_tiles[i + 1][j - 1].adjacentFlags += to_add
            case 4:
                window.list_of_tiles[i][j + 1].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j + 1].adjacentFlags += to_add
                window.list_of_tiles[i + 1][j].adjacentFlags += to_add
                window.list_of_tiles[i + 1][j + 1].adjacentFlags += to_add
            case 5:
                window.list_of_tiles[i][j + 1].adjacentFlags += to_add
                window.list_of_tiles[i][j - 1].adjacentFlags += to_add
                window.list_of_tiles[i + 1][j + 1].adjacentFlags += to_add
                window.list_of_tiles[i + 1][j].adjacentFlags += to_add
                window.list_of_tiles[i + 1][j - 1].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j + 1].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j - 1].adjacentFlags += to_add
            case 6:
                window.list_of_tiles[i][j - 1].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j - 1].adjacentFlags += to_add
                window.list_of_tiles[i + 1][j].adjacentFlags += to_add
                window.list_of_tiles[i + 1][j - 1].adjacentFlags += to_add
            case 7:
                window.list_of_tiles[i][j + 1].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j + 1].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j].adjacentFlags += to_add
            case 8:
                window.list_of_tiles[i][j - 1].adjacentFlags += to_add
                window.list_of_tiles[i][j + 1].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j - 1].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j + 1].adjacentFlags += to_add
            case 9:
                window.list_of_tiles[i][j - 1].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j - 1].adjacentFlags += to_add
                window.list_of_tiles[i - 1][j].adjacentFlags += to_add
root = tk.Tk()
window = Window(root)
root.mainloop()