"""

"""

from tkinter import *


class HangmanGame:
    def __init__(self):
        self.__window = Tk()
        self.__window.title("Hangman -game")

        self.__turn = None
        self.__mistakes = None



    def start(self):
        self.__window.mainloop()


def main():
    ui = HangmanGame()
    ui.start()


main()
