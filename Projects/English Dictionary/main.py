
# %% Imports
import json
import difflib

def translate(word , words_dict):
    word = word.lower()
    if word in words_dict:
        return words_dict[word]
    else:
        print("Word does not exist, Please check it.")

difflib.SequenceMatcher()
words_dict = json.load(open("data.json" , "r"))             #loading json file data
word = input("Enter a word to search : ")
print(translate(word, words_dict))







