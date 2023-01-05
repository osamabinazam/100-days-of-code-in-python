
import  random as r

# list of words
word_list = ["gone" ,"play" ,"go","secret" ,"ambitions","hello","world"]
random_word = r.choice(word_list)
guessed_letter = []                    # list used to add guessed numbers

# Printing Stuff
print("Word list is : " , word_list,"\n")
for letter in random_word:
    guessed_letter +="_"
print(guessed_letter)
print("Guess " + str(len(random_word) )+ " letters")

# Logic Implementation
while True:
    guess = input("Guess a word: ")     # prompt user to enter his/her guess
    guess = guess.strip().lower()       # converting input into desired format
    index = random_word.find(guess)     # Get the index of letter in random word
    for letter in random_word:
        if letter== guess:
            guessed_letter[index] = guess
            print(guessed_letter,"\n")
    if guess not in random_word:
        print("Oops!, You've guessed wrong letter please try again")
    if "_" not in guessed_letter:
         break

print("Guessed Letters are : ",guessed_letter)