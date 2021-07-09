from player import Player
from tkinter import *

class PopIt:

    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0]]
        self.buttons_pressed = 0
        self.whose_turn = None
        self.game_over = False
        self.loser = None
        self.buttonsList = [[],[],[],[],[],[]]

    def if_clicked_square(self, i, j):

        print(str(i) + " " + str(j))
        if self.board[i][j] == 0:
            self.board[i][j] = 1
            self.buttonsList[i][j]["text"] = "1"
            self.buttons_pressed += 1

        else:
            self.board[i][j] = 0
            self.buttonsList[i][j]["text"] = "0"
            self.buttons_pressed -= 1

        if self.buttons_pressed > 1:
            return

        else:
            for m in range(0,6):
                if m != i:
                    continue
                else:
                    for n in range(0, len(self.board[m])):
                        b = self.buttonsList[m][n]
                        b["state"] = "disabled"

    def if_clicked_confirm(self):
        num_gone = 0

        for i in range(0,6):
            for j in range(0, len(self.board[i])):
                if self.board[i][j] == 1:
                    b = self.buttonsList[i][j]
                    b["state"] = "disabled"
                    num_gone += 1
                else:
                    b = self.buttonsList[i][j]
                    b["state"] = "normal"
        if num_gone == 28:
            self.game_over = True
            self.loser = self.whose_turn
            return

        if self.whose_turn == 1:
            self.whose_turn = 2
        else:
            self.whose_turn = 1

    def run_game(self):

        root = Tk()

        confirm_button = Button(root, text="Confirm Move", height=4, width=10, command=lambda: self.if_clicked_confirm())
        confirm_button.place(x=100, y = 700)

        for i in range(0, 6):
            for j in range(0, len(self.board[i])):
                button = Button(root, text="0", height=2, width=10, command=lambda: self.if_clicked_square(i, j))
                button.place(x=25 + (100 * j), y=100 + (100 * i))

                # button.pack()
                self.buttonsList[i].append(button)

        root.mainloop()

pop = PopIt()

pop.run_game()

