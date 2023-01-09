
# Converting a string into dictionary as key and value corresponde to key is
# the amount of that letter in the string
my_str = "Hello World"
my_dict = {}
for letter in my_str:
    my_dict[letter] = my_dict.get(letter, 0) + 1

print(my_dict)
