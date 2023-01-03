# zip() takes any number of iterables and returns a zip object that is an iterator of tuples.
# If you wanted to print the values of a zip object, you can convert it into a list and then print it.
# Printing just a zip object will not return the values unless you unpack it first.


# Creating three list
names = ["Osama", "Shahzaman", "Shafique", "Saad"]
weights = [50, 45, 40, 60]
age = [23, 22, 22, 21]

# creating a list of lists using zip method
listOfList = list(zip(names, weights, age))  # Conveting zip object into list directly

# Printing
print(listOfList)

# Creating zip object first
zip_object = zip(names, weights, age)

# Trying to print the zip but it will print reference in the memory
print(zip_object)

# Unpacking the zip object
for value1,value2,value3 in zip_object:
    print("\nName is : " , value1 , "\nWeight is : ",value2,"\nAge is : ",value3)