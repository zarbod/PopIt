from player import Player
import time
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
        qb = self.buttonsList[i][j]
        print(str(i) + " " + str(j))
        if self.board[i][j] == 0:
            self.board[i][j] = 1
            qb["text"] = "1"
            self.buttons_pressed += 1

        else:
            self.board[i][j] = 0
            qb["text"] = "0"
            self.buttons_pressed -= 1

        if self.buttons_pressed > 1:
            return

        else:
            for m in range(0,6):
                if m == i:
                    continue
                else:
                    for n in range(0, len(self.board[m])):
                        b = self.buttonsList[m][n]
                        b["state"] = "disabled"

    def if_clicked_confirm(self):
        num_gone = 0

        for i in range(0, 6):
            for j in range(0, len(self.board[i])):
                b = self.buttonsList[i][j]
                if self.board[i][j] == 1:
                    b["state"] = "disabled"
                    num_gone += 1
                else:
                    b["state"] = "normal"
        if num_gone == 28:
            self.game_over = True
            self.loser = self.whose_turn
            return

        self.buttons_pressed = 0

        if self.whose_turn == 1:
            self.whose_turn = 2
        else:
            self.whose_turn = 1

    def run_game(self):

        root = Tk()

        player1 = Player()
        player2 = Player()

        confirm_button = Button(root, text="Confirm Move", height=4, width=10, command=lambda: self.if_clicked_confirm())
        confirm_button.place(x=100, y = 700)

        for i in range(0, 6):
            for j in range(0, len(self.board[i])):

                button = Button(root, text="0", height=2, width=10, command=lambda i1 = i, j1 = j: self.if_clicked_square(i1,j1))
                button.place(x=25 + (100 * j), y=100 + (100 * i))

                # button.pack()
                self.buttonsList[i].append(button)

        while True:
            if self.game_over:
                print("Game Over")
                label = Label(root, text="Game Over", font=30, height=5, width=15)
                label_win = Label(root, font=15, height=5,width=15)
                label_win.place(x=700,y=400)
                label.place(x=700, y=250)
                win_text = ""
                if self.loser == 1:
                    win_text = "Player 2 Wins!"
                    player2.set_score(player2.get_score() + 1)
                else:
                    win_text = "Player 1 Wins!"
                    player1.set_score(player1.get_score() + 1)

                win_text += "\n Player 1 score: " + str(player1.get_score()) + "\n Player 2 score: " + str(player2.get_score())

                label["text"] = win_text

                root.update()
                time.sleep(5)
                return

            else:
                root.update()


pop = PopIt()

pop.run_game()


