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


# Unzipping means converting the zipped values back to the individual self as they were.
# This is done with the help of “*” operator. So now, if we want to put the old values into
# result1 and result2 from zipped list zip1, then we have to unzip zip1.

print("\nUnziping a ziped object using '*':\n")

surnames = ["Arain", "Abbasi","Mirani" ,"Pathan"]
# Create a zip object from name and surname: z1
zip1 = zip (names,surnames)

# Print the tuples in z1 by unpacking with *
print("Names with Surnames: ",*zip1)
# Re-create a zip object from mutants and powers: z1
z1 = zip(names,surnames)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print("Names : ",result1)
print("Surnames : ",result2)

