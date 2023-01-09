
# A dictionary can have a dictionary/dictionaries associated with a key
# The key must be of any type
# The value can be a dictionary, list , etc

cars = {
    1:{
        "Name": "Ford",
        "Model": "Mastang",
        "Color": "Brown",
        "Year": 2010,
        "Country": "USA",
        "Electric":False
    },
    2 :{
        "Name": "Nisan GTR",
        "Model": "R-35 Nismo",
        "Color": "Black",
        "Year": 2020,
        "Country": "Japan",
        "Electric":True
    }
}

print("Nested Dictionary is : ", cars)

# Accessing item in the nested Dictionary
car1 = cars[1];
print("\nThe keys of dictionary at index 1 is : ", car1.keys())
print("The values of dictionary at index 1 is : ", car1.values())

# Accessing item in the nested Dictionary
car2 = cars[2];
print("\nThe keys of dictionary at index 2 is : ", car2.keys())
print("The values of dictionary at index 2 is : ", car2.values())

# looping through the whole dictionary
def printdic(cars):
    for outer_key, values in cars.items():
        print("\nCar",outer_key," Detail is : ")
        for inner_key,value in values.items():
            print("Key: Value =  " ,inner_key," ",value)
            # print("The value corresponds to outer key is also a dictionary: ", inner_key)
            # print("The value corresponds to inner dictionary is : ", value)

printdic(cars)          # printing the whole dictionary by calling printdic() function
print("\nAfter adding another car our dictionary become:")
# Adding another dictionary to the dictionary
car3 ={"Name": "Lamborghini", "Model": "Avendator", "Color": "White","Electric":False}
cars[3]=car3                                    # Adding using index
car4 ={"Name": "Toyota", "Model": "Corolla", "Color": "Red", "Electric":False, "Year":2007}
cars.update({4:car4})                           # Adding using update methed
printdic(cars)      # printing the whole dictionary by calling printdic() function

print("\nRemoving items from the dictionary: ")
# deleting an item from outer dictionary
del cars[4]
# deleting an item from inner dictionary
del cars[3]["Electric"] # deleting
printdic(cars)  # printing the whole dictionary by calling printdic() function


