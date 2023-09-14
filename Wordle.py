# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        entered_word = s.lower()

        #check if entered word is found in dictionary
        if entered_word in FIVE_LETTER_WORDS:
            gw.show_message("Great Choice!")
        else:
            gw.show_message("Not in word list.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Choose a random word from FIVE_LETTER_WORDS
    random_word = random.choice(FIVE_LETTER_WORDS).upper()

    # Display the chosen word in the first row of boxes (row 0)
    # for i in range(len(random_word)):
    #     gw.set_square_letter(0, i, random_word[i])

# Startup code

if __name__ == "__main__":
    wordle()
