# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    # Choose a random word from FIVE_LETTER_WORDS
    random_word = random.choice(FIVE_LETTER_WORDS).lower()
    print(random_word)

    def color_boxes(random_word,entered_word):
        for i in range(0,5):
            if random_word[i] == entered_word[i]:
                gw.set_square_color(gw.get_current_row(),i,"#66BB66")
            elif (entered_word[i] in random_word) and (random_word[i] != entered_word[i]):
                gw.set_square_color(gw.get_current_row(),i,"#CCBB66")
            else:
                gw.set_square_color(gw.get_current_row(),i,"#999999")


    def enter_action(s):
        entered_word = s.lower()

        #check if entered word is found in dictionary
        if entered_word not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
        elif entered_word == random_word:
            gw.show_message("You Won")
            color_boxes(random_word,entered_word)
        else:
            color_boxes(random_word,entered_word)
            gw.set_current_row(gw.get_current_row() + 1)

    

    gw = WordleGWindow()

    gw.add_enter_listener(enter_action)


    # # Display the chosen word in the first row of boxes (row 0)
    # for i in range(len(random_word)):
    #    gw.set_square_letter(0, i, random_word[i])

# Startup code

if __name__ == "__main__":
    wordle()