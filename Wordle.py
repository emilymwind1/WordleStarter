# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

MAX_GUESSES = 6


def wordle():

    def get_color_scheme():
        choice = input("Choose a color scheme (traditional or colorblind): ").strip().lower()
        if choice in ["traditional", "colorblind"]:
            return choice
        else:
            print("Invalid choice. Please choose either 'traditional' or 'colorblind'.")

    color_scheme = get_color_scheme()
    print(color_scheme)

    # Choose a random word from FIVE_LETTER_WORDS
    random_word = random.choice(FIVE_LETTER_WORDS).lower()
    print(random_word)

    def color_boxes(random_word,entered_word,color_scheme):

        if color_scheme == "traditional":
            correct_position = "#66BB66"
            incorrect_position = "#CCBB66"
        else:
            correct_position = "#0000FF"
            incorrect_position = "#FF0000"

        for i in range(0,5):
            if random_word[i] == entered_word[i]:
                gw.set_square_color(gw.get_current_row(),i, correct_position)
            elif (entered_word[i] in random_word) and (random_word[i] != entered_word[i]):
                gw.set_square_color(gw.get_current_row(),i,incorrect_position)
            else:
                gw.set_square_color(gw.get_current_row(),i,"#999999")
            
            #function to tell the user they are out of guesses
            if gw.get_current_row() == MAX_GUESSES -1 and entered_word != random_word:
                gw.show_message(f"Out of guesses! The word was: {random_word} \nBetter Luck Next Time! \nPress Esc to exit")


    def enter_action(s):
        entered_word = s.lower()
        numTries = gw.get_current_row() +1

        #check if entered word is found in dictionary
        if entered_word not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
        elif entered_word == random_word:
            gw.show_message(f"You Won! \nYou guessed the word in {numTries} guesses! \nPress Esc to exit")
            color_boxes(random_word,entered_word,color_scheme)
        else:
            color_boxes(random_word,entered_word,color_scheme)
            gw.set_current_row(gw.get_current_row() + 1)

            print(gw.get_current_row())

    

    gw = WordleGWindow()

    gw.add_enter_listener(enter_action)

    # Allow the player to exit the game by pressing Esc
    gw._root.bind("<Escape>", lambda event: gw._root.destroy())

    #Allow the player to play again
    # gw._root.bind("<Tab>", lambda event: gw._root.mainloop())


    # # Display the chosen word in the first row of boxes (row 0)
    # for i in range(len(random_word)):
    #    gw.set_square_letter(0, i, random_word[i])

# Startup code

if __name__ == "__main__":
    wordle()