"""

"""

from tkinter import *


HANGMANPICS = ["Hangman_start.gif", "Hangman_step1.gif", "Hangman_step3.gif",
               "Hangman_step4.gif", "Hangman_step5.gif", "Hangman_step6.gif",
               "Hangman_step7.gif", "Hangman_final.gif"]

PLAYER1 = 1
PLAYER2 = 2

ALPHABET = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "å", "a", "s",
            "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "z", "x", "c", "v",
            "b", "n", "m"]


class HangmanGame:
    def __init__(self):
        self.__window = Tk()
        self.__window.title("Hangman -game")

        self.__turn = None
        self.__mistakes = None

        self.__hangmanpics = []
        for picturefile in HANGMANPICS:
            picture = PhotoImage(file=picturefile)
            self.__hangmanpics.append(picture)

        self.__letterbuttons = {}
        for letter in ALPHABET:
            button = Button(self.__window, text=letter, width=2,
                            command=lambda y=letter: self.keyboard_input(y))
            self.__letterbuttons[letter] = button

        self.__keyboard_info = Label(self.__window, text="Guess letters!")
        self.__word_entry = Entry()
        self.__word_to_guess = self.__word_entry
        self.__word_entry.grid(row=17, column=4, columnspan=5)

        self.__entrylabel = Label(self.__window, text="Enter word:")
        self.__entrylabel.grid(row=17, column=0, columnspan=3)
        self.__StartgameButton = Button(self.__window, text="Start the game!",
                                        command=self.initialize_game)
        self.__StartgameButton.grid(row=17, column=9)

        Button(self.__window, text="Quit", command=self.__window.destroy)\
            .grid(row=17, column=26)

        self.__pictureLabel = Label(self.__window)
        self.__pictureLabel.grid(row=0, column=0, rowspan=16, columnspan=10)




    def initialize_game(self):
        self.__turn = PLAYER1
        self.__pictureLabel.configure(image=self.__hangmanpics[0])
        word_entry = self.__word_entry.get()
        self.__word_entry.delete(0, END)
        self.__word_entry.insert(0, "*" * len(word_entry))
        self.__word_entry.configure(state=DISABLED)
        self.__keyboard_info.grid(row=3, column=11)
        self.__entrylabel.configure(text="Guess this word")
        self.__StartgameButton.configure(text="Reset")
        self.setup_keyboard()



    def keyboard_input(self, key):
        self.__letterbuttons[key].configure(state=DISABLED)


    def start(self):
        self.__window.mainloop()

    def setup_keyboard(self):
        row = 4
        column = 12
        while row <= 6:
            if row == 4:
                for index in range(ALPHABET.index("a")):
                    self.__letterbuttons[ALPHABET[index]].grid(row=row, column=column)
                    column += 1

            if row == 5:
                for index in range(ALPHABET.index("a"), ALPHABET.index("z")):
                    self.__letterbuttons[ALPHABET[index]].grid(row=row, column=column)
                    column += 1

            if row == 6:
                column = 14
                for index in range(ALPHABET.index("z"),
                                   ALPHABET.index("m") + 1):
                    self.__letterbuttons[ALPHABET[index]].grid(row=row, column=column)
                    column += 1

            column = 12
            row += 1


def main():
    ui = HangmanGame()
    ui.start()


main()
