import random
from words import words
import string

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()


def hang_man():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')  
            else:
                lives -= 1
                print('Letter is not in the word.')
        elif user_letter in used_letters:
            print('You have already used that letter. Try again.')
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print(f"\nYou died, sorry. The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}")


hang_man()
