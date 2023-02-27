# Reading a file
# Open () function create an object of file and returned it
# Returned Object has a function called read that help to read content of the file and read() return content as a String Object

myfile = open("fruits.txt", mode="r")
content = myfile.read()
print("Type of myfile object is : " , type(myfile))             # return the name of the classs
myfile.close()                                                  # close the file object


print("Type of myfile.read() is : ", type(content))             # return String Object
print("Content of the file is : \n" ,content)

# Optimum and Orgranized way
# Process file here and then close
with open("fruits.txt" , mode="r") as myfile:
    content = myfile.read()
    myfile.close()

print("\nContent of the file is : \n", content)

# Writing content to file
# If file is exist then the content of the file will be overridden
with open("vagetables.txt" , mode="w") as myfile:
    myfile.write("Tomato\nCarrot\nBringle")



