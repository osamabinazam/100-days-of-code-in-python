# Required libraries
import random
import time
import Hangman_art
import Hangman_words
import replit
from os import system,name


#
def userAndLogo(playername, lives):
    print("\t" + Hangman_art.logo)
    print("*=========================================")
    print(f"*\tPlayer :{playername}")
    print(f"*\tLives  :{lives}")
    print("*==========================================")


def greeting():
    # Greeting and Welcoming the user
    print(Hangman_art.logo + "\n\n", "Welcome to \"Hangman\" Game developed by \"Osama Bin Azam\"\n")
    user = input("What is your name ? : ")
    print("Hello " + user + "! Time to play Hangman!")
    # time.sleep(3)
    print("The Game is about to start have patience\nBest of Luck")
    # time.sleep(3)
    return user


def hangman(word_list, username, lives):
    end = False
    random_word = random.choice(word_list)
    display_letters = []
    for let in random_word:
        display_letters += "_"
    print("Word is : ",''.join(display_letters))

    while True:
        guess = input("Guess a word: ")  # prompt user to enter his/her guess
        clearScreen()                    #Clear Terminal
        userAndLogo(username, lives)
        guess = guess.strip().lower()  # converting input into desired format
        index = random_word.find(guess)  # Get the index of letter in random word
        if guess in display_letters:
            print(f"You've already guess {guess} ")

        for letter in random_word:
            if letter == guess:
                display_letters[index] = guess

        # When Guessed is not in the random word
        if guess not in random_word:

            lives = lives - 1;
            clearScreen()
            userAndLogo(username, lives)
            print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")
            if lives == 0:
                end = True
                print("Oops!, You lose")

        print(Hangman_art.stages[lives])
        print("Word is : ", ''.join(display_letters))
        print(f"You've guessed {guess}\n")

        # When no more dash left in the list: guessed_letters
        if "_" not in display_letters:
            print("Word is : ", ''.join(display_letters))
            print("You Win The Game")
            playAgain()
        if end:
            playAgain()


def playAgain():
    clearScreen()
    choice = input("Wanna play again ? (Yes/No) (yes/no) (Y/N) (y/n)")
    if choice in ["yes", "Yes", "Y", "y"]:
        Main()
    elif choice in ["No", "no", "N", "n"]:
        print("Thanks\nBye")
        exit(0)
    else:
        playAgain()


# This method will world on linux, Mac and windows terminals
def clearScreen ():
    # for windws powershell or cmd
    print("In Clear")
    if name == 'ut':
        system('cls')
    #for windows , linux and Mac terminals
    else:
        print("in Else")
        system('clear')
def Main():
    total_lives = 6
    username = greeting()
    clearScreen()
    userAndLogo(username, total_lives)
    word_list = Hangman_words.word_list
    hangman(word_list, username, total_lives)


Main()

