'''
Hang man
********
'''

import random
import string
from words import words



def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def play():
    
    lives = 6
    word_to_guess = get_valid_word(words)
    word_letters = set(word_to_guess)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # Keep track of what is guessed

# Base case for game: 


    while len(word_letters) > 0 and lives > 0:
        # show the user what letters thwy have used:
        print("You have used these letters: ", " ".join(used_letters))
        # what is the the current W - R D

        # word_list as List comprehension
        word_list = [letter if letter in used_letters else '-' for letter in word_to_guess]

        # word_list as For Loop
        # word_list = []
        # for letter in word_to_guess:
        #     if letter in used_letters:
        #         word_list.append(letter)
        #     else:
        #         word_list.append('-')
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        # if the guess is in the alphabet(less the used letters)
        # add the guess to used letters set
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"You just lost a life only {lives} / 6 remain...")

        elif user_letter in used_letters:
            print("You have already used that letter: Try again: ")
        else:
            print("You need to print a valid character")
    if lives == 0:
        print("Sorry the man was hung! The word was", word_to_guess)
    else:
        print("You have guess the word:", word_to_guess)
        
play()
