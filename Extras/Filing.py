# Reading a file
# Open () function create an object of file and returned it
# Returned Object has a function called read that help to read content of the file and read() return content as a String Object

myfile = open("./files/fruits.txt", mode="r")
content = myfile.read()
print("Type of myfile object is : " , type(myfile))             # return the name of the classs
myfile.close()                                                  # close the file object


print("Type of myfile.read() is : ", type(content))             # return String Object
print("Content of the file is : \n" ,content)

# Optimum and Orgranized way in which we don't have to close file object manually
# Process file here and then close
with open("./files/fruits.txt" , mode="r") as myfile:
    content = myfile.read()


print("\nContent of the file is : \n", content)

# Writing content to file
# "w" -> If file is exist then the content of the file will be overridden
# "x" -> If file is exist then an error will be thrown
with open("./files/vagetables.txt" , mode="w") as myfile:
    myfile.write("Tomato\nCarrot\nBringle")


# Appending content to file
# "a" -> use to append con tent to the file and updates it
with open("./files/vagetables.txt" , "a") as myfile:
    myfile.write("\nGarlic")

del myfile
# we can not read from and write to file using same object.
# To do so, we use "a+" mode which let us write/read operation on a same object
# we also use seek() method that let us change the position of the cursur
with open("./files/fruits.txt" ,"a+") as myfile:
    myfile.write("\nWatermelon")
    content = myfile.read()
print("The content of the file is : " , content)


