
# The value of the key can be of any type such as integer, float, list.
# But type of keys should be same

hetro_dict = {
    "Name" :"Ford",
    "Electric ": False,
    "Model" : "Mastang",
    "Milage": 10,
    "colors" : ["red", "blue", "green"]
}

# looping through dictionnary in traditional way
# But it will only read the keys
for  thing in hetro_dict:
    print("Key and value = ",thing,":", hetro_dict[thing])


# .items() function will return a tuple of (key, value) pairs
for key, value in hetro_dict.items():
    print("Key : Value = ", key,":" , value)

# Looping through the list of keys
print("\nList of keys are : " , end=" ")
for key in  hetro_dict.keys():
    print(key,end=" ")

# Looping through the list of values
print("\nList of values are : " , end=" ")
for values in hetro_dict.values():
    print(values, end=" ")
