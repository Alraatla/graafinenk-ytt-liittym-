"""

"""

from tkinter import *


HANGMANPICS = ["Hangman_start.gif", "Hangman_step1.gif", "Hangman_step3.gif",
               "Hangman_step4.gif", "Hangman_step5.gif", "Hangman_step6.gif",
               "Hangman_step7.gif", "Hangman_final.gif"]

PLAYERS = 2

ALPHABET = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "å", "a", "s",
            "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "z", "x", "c", "v",
            "b", "n", "m"]


class HangmanGame:
    def __init__(self):
        self.__window = Tk()
        self.__window.title("Hangman -game")

        self.__turn = None
        self.__mistakes = 0
        self.__word_to_guess = None
        self.__player_scores = [0] * PLAYERS

        self.__hangmanpics = []
        for picturefile in HANGMANPICS:
            picture = PhotoImage(file=picturefile)
            self.__hangmanpics.append(picture)

        self.__letterbuttons = {}
        for letter in ALPHABET:
            button = Button(self.__window, text=letter, width=2,
                            command=lambda y=letter: self.keyboard_input(y))
            self.__letterbuttons[letter] = button
        
        for number in range(PLAYERS)
            Label(self.__window, text="Player {:1s} score:".format(str(number + 1)))\
            .grid(row=number + 15, column=11)
        
        self.__pointlabels =[]
        for number in range(PLAYERS):
            label = Label(self.__window)
            label.grid(row=number + 15, column=12)
            self.__pointlabels.append(label)
        
        self.__keyboard_info = Label(self.__window, text="Guess letters!")
        self.__word_entry = Entry()
        self.__word_to_guess = None
        self.__word_guessed = []
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
        self.__turn = 1
        self.__pictureLabel.configure(image=self.__hangmanpics[self.__mistakes])
        self.__word_to_guess = self.__word_entry.get().lower()
        self.__word_guessed = list(
            map(lambda x: "*", range(len(self.__word_to_guess))))
        self.__keyboard_info.grid(row=3, column=11)
        self.__entrylabel.configure(text="Guess this word")
        self.__StartgameButton.configure(text="Reset", command=self.reset_turn)
        self.setup_keyboard()
        self.update_ui()

    def reset_turn(self):

        self.__word_guessed = list(
            map(lambda x: "*", range(len(self.__word_to_guess))))
        self.__mistakes = 0
        self.setup_keyboard()
        self.update_ui()

    def keyboard_input(self, key):
        self.__letterbuttons[key].configure(state=DISABLED)
        for index in range(len(self.__word_to_guess)):
            if key == self.__word_to_guess[index]:
                self.__word_guessed[index] = key
        if key not in self.__word_to_guess:
            self.__mistakes += 1
        self.update_ui()
        self.check_end_of_turn()


    def start(self):
        self.__window.mainloop()

    def setup_keyboard(self):
        row = 4
        column = 12
        while row <= 6:
            if row == 4:
                for index in range(ALPHABET.index("a")):
                    self.__letterbuttons[ALPHABET[index]].grid(row=row, column=column)
                    self.__letterbuttons[ALPHABET[index]].configure(state=NORMAL)
                    column += 1

            if row == 5:
                for index in range(ALPHABET.index("a"), ALPHABET.index("z")):
                    self.__letterbuttons[ALPHABET[index]].grid(row=row, column=column)
                    self.__letterbuttons[ALPHABET[index]].configure(state=NORMAL)
                    column += 1

            if row == 6:
                column = 14
                for index in range(ALPHABET.index("z"),
                                   ALPHABET.index("m") + 1):
                    self.__letterbuttons[ALPHABET[index]].grid(row=row, column=column)
                    self.__letterbuttons[ALPHABET[index]].configure(state=NORMAL)
                    column += 1

            column = 12
            row += 1

    def update_ui(self):
        self.__word_entry.configure(state=NORMAL)
        self.__word_entry.delete(0, END)
        self.__word_entry.insert(0, " ".join(self.__word_guessed))
        self.__word_entry.configure(state=DISABLED)
        self.__pictureLabel.configure(
            image=self.__hangmanpics[self.__mistakes])
        for i in range(len(self.__pointlabels)):
            self.__pointlabels[i].configure(text=self.__player_points[i])

    def check_end_of_turn(self):
        if self.__mistakes == 8:
            self.__player_scores[self.__turn % 2] += 1
            self.__turn += 1
        if "*" not in self.__word_guessed:
            if self.__turn % 2 == 0:
                self.__player_scores[0] += 2
            else:
                self.__player_scores[1] += 2
            self.__turn += 1
        self.update_ui()

def main():
    ui = HangmanGame()
    ui.start()


main()
