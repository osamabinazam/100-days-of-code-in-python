# Dictionary
programming_dictionary = {
    "Bug": "An error in the program that stop the execution of program",
    "Function": "A piece of code that can be executed",
    "Looping": "A piece of code that can be executed repeatedly"
}

# Retrieving a value from a dictionary using key
# Data type of keys and index during retirieval should be same otherwise
# typeErr will be raised
print("Key is Bug : " + programming_dictionary["Bug"])
print("Key id Function : " + programming_dictionary["Function"])

# Printing the whole dictionary
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# wiping an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# adding elements to empty_dictionary
empty_dictionary["Bug"] = "An error in the program that stop the execution of program"
empty_dictionary["Function"] = "A piece of code that can be executed"
empty_dictionary["Looping"] = "A piece of code that can be executed repeatedly"
print("Elements of empty dictionary \n",empty_dictionary)

