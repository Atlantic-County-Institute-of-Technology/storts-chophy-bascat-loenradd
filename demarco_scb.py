# Leonard DeMarco, 11/3/25 - 11/13/25, Storts Chophy Bascats

import random
import os
import math

word_list = []  # evil list of words that are word_length long

def main():
    did_i_win_yet = False  # Bool to determine if user guessed correctly already, helps break out of loop
    target_word = ""  # Clear target word var

    os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
    try:  # Vals defined with abs() to avoid negatives
        word_length = abs(int(input("[-] Input how long you would like the word to be. Maximum length 25 : ")))
        if word_length > 25: #
            input("[!] Please input a length less than or equal to 25.")
            main()
        guess_amount = abs(int(input("[-] Input how many guesses you would like : ")))
    except ValueError:  # Tomfoolery prevention
        input("[!] Please input a valid integer.")
        main()

    try:
        with open("assets/words_alpha.txt", "r") as file:  # Open file with all words
            for word in file:
                if len(word) == word_length + 1:  # Check length of all words in file (+ 1 to account for newline)
                    word_list.append(word.strip())  # Get all words that are word_length long
            target_word = word_list[random.randint(0, len(word_list))]  # Chose a random word from the stripped list
    except FileNotFoundError:
        print("aw dangit!")
        quit()  # Die if file fetch fails

    guess = 0  # Determine how many guesses user has made
    answer_list = list(target_word)  # Break target word into list so we can examine individual letters
    stringer = ""  # String that will be used to display user guesses

    guess_array = []  # Clear prev answers
    for i in range(0, guess_amount):
        guess_array.append(str("_" * word_length + " | " + "#" * word_length))  # Construct array based on length of target word

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
        for i in range(guess_amount+1):  # Print menu (+1 to account for header)
            if i == 0:
                print("-- wordle real hard moder-- \n~{ X = hit, Y = wrong spot, 0 = not in word }~")
            else:
                print(guess_array[i-1])
        if guess == guess_amount or did_i_win_yet:  # Check if user won or used up all guesses
            print(f"\nThe word was {target_word.upper()}.")
            restart = input("Would you like to play again? y/n: ")
            if restart == "y":
                main()  # Play again
            else:
                quit()

        guess_input = input("\n[!] - make yo guess : ")

        if guess_input == target_word:
            did_i_win_yet = True

        if len(guess_input) != word_length:  # Tomfoolery prevention
            input(f"[!] - Please make your guess {word_length} characters long.")
        elif guess_input not in word_list:
                input("[!] - Not in word list. Press Enter to continue.")
        else:
            guess_list = list(guess_input)  # Break user's guess into a list to compare with answer_list

            response = f"{guess_input} | "

            for i in range(word_length):
                if guess_list[i] == answer_list[i]:
                    response = f"{response}X"
                elif guess_list[i] != answer_list[i] and guess_list[i] in answer_list:
                    response = f"{response}Y"
                else:
                    response = f"{response}O"
            guess_array[guess] = response
            guess += 1


input(
        """
________________________________________________________________________________________
                 _     _                _        ___ ___ _     _     _    ___   ___ ___ 
 _ _ _ ___ ___ _| |___| |   ___ ___ ___| |   ___|  _|  _|_|___|_|___| |  |_  | |   |   |
| | | | . |  _| . | -_| |  |  _| -_| .'| |  | . |  _|  _| |  _| | .'| |   _| |_| | | | |
|_____|___|_| |___|___|_|  |_| |___|__,|_|  |___|_| |_| |_|___|_|__,|_|  |_____|___|___|
---------------------------------------------------------------------------------------- \n
                            press enter to le start
        """
    )  # legally distinct
main()
