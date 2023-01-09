
# Dictionary of heights
students_height = {
    "Osama": 5.4,
    "Shazaman": 5.2,
    "Shafique": 5.2,
    "Izzah":4.8
}
# Dictionary can also be created using dict() constructor
# key = Umar
# value = 5.4
teachers_height = dict(Umar=5.4, Saif=5.2,Khalid=5.6)

# Values of dictionary can be access using get() function
print("Printing Values Using get() function:", end=" ")
print(students_height.get("Osama"), end=" ")
print(students_height.get("Shazaman"),end=" ")
print(students_height.get("Shafique"),end=" ")
print(students_height.get("Izzah"),end=" \n")

# keys() function will return a list consist of all keys of the dictionary
# values() function do the same as keys() but returns a list of all values
list_of_keys = students_height.keys()
list_of_values= students_height.values()
print("Keys  = ", list_of_keys)
print("Values = ", list_of_values)

# if construct for dictionaries
if "Osama" in students_height:
    print("Osama is in dictionary and his height is : " , students_height.get("Osama"))

# The update() method will update the dictionary with the
# items from the given argument.
students_height.update({"Osama" : 5.6})
print("Osama's Height is  : ", students_height.get("Osama"))

# adding a pair of key and value in the list
# we can also update method to add element in the element
students_height["Ayesha"] = 5.0
students_height.update({"Maria" : 5.1}  )
students_height.update({"Hanzla": 5.2}  )
print("Ayesha's Height is  : ", students_height.get("Ayesha"))
print("Maria's Height is  : ", students_height.get("Maria"))
print("Hanzla's Height is  : ", students_height.get("Hanzla"))

# Removing an element from the disction
# The pop() method removes the item with the specified key name
# Before removing
list_of_keys = students_height.keys()
list_of_values= students_height.values()
print("Keys  = ", list_of_keys)
print("Values = ", list_of_values)

# pop out Hanzla and Ayesha
students_height.pop("Hanzla")
students_height.pop("Ayesha")

# After
list_of_keys = students_height.keys()
list_of_values= students_height.values()
print("Keys  = ", list_of_keys)
print("Values = ", list_of_values)

# In python >3.7, popitem() function remove last inserted item from the dictionary
# Python <=3.7 popitem() function remove random item from the dictionary
students_height.popitem()
print("Students height is : " , students_height.values())

# del keyword also used to remove an item from the dictionary
del students_height["Osama"]
print("Osama's Height is  : ", students_height.get("Osama"))

# # fromkeys() is used to retrieve value of specified key
# # It returns a dictionary with specified value
# specified_keys= students_height.fromkeys("Izzah")
# print(specified_keys)
# for key,value in specified_keys.items():
#     print("Values corresponds to specified key is :",key,value)

# clear method will clear the dictionary
students_height.clear()
print("Students Names are       : ", students_height.values())
print("Students heights are     : ", students_height.values())



