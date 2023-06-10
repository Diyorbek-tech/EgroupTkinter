from tkinter import *
from tkinter.messagebox import *


class TicTacToe:
    def __init__(self):
        self.oyna = Tk()
        self.oyna.geometry('650x450')
        self.oyna.title('X vs O')

        # Store the buttons in a dictionary instead of individual variables
        self.buttons = {}
        for row in range(3):
            for col in range(3):
                btn = Button(self.oyna, text='', width=10, height=5, font=('Arial', 16),
                             command=lambda row=row, col=col: self.click(row, col))
                btn.grid(row=row, column=col)
                self.buttons[(row, col)] = btn

        # Store the score as class attributes instead of global variables
        self.user1_score = 0
        self.user2_score = 0

        self.count = 0
        self.current_player = 'X'

    def click(self, row, col):
        # Check if the button is empty
        if self.buttons[(row, col)]['text'] == '':
            # Set the button text to the current player
            self.buttons[(row, col)]['text'] = self.current_player
            self.count += 1
            # Check for a winner or a draw
            self.find_winner()
            # Switch the current player
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def find_winner(self):
        # Check for all possible winning combinations
        for (a, b, c) in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]:
            if self.buttons[(a//3, a%3)]['text'] == self.buttons[(b//3, b%3)]['text'] == self.buttons[(c//3, c%3)]['text'] != '':
                # Display a message box for the winner
                winner = self.buttons[(a//3, a%3)]['text']
                showinfo("Game Over", f"{winner} wins!")
                # Reset the game
                self.reset()
                return
        if self.count == 9:
            # Display a message box for a draw
            showinfo("Game Over", "It's a draw!")
            # Reset the game
            self.reset()

    def reset(self):
        # Set the button text to empty and reset the count and current player
        for btn in self.buttons.values():
            btn['text'] = ''
        self.count = 0
        self.current_player = 'X'


tictactoe = TicTacToe()
tictactoe.oyna.mainloop()