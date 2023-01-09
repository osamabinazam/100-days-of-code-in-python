
# List of dictionaries
item_list = [
    {
        "Fruite" : "Apple" ,
        "Amount" : 200
    } ,
    {
        "Fruite" : "Orange",
        "Amount" : 300
    },
    {
        "Mobile": "Samsung",
        "Amount": 2000
    }
]

print("\nPrinting list of dictionaries:")
# Printing the list of dictionaries
for i in item_list:
    for key, value in i.items():
        print(key, value)

# Combining values into list
values_list =[]
for i in item_list:
    for key, value in i.items():
        values_list.append(value)

del item_list
# Printing the list of values
print("\nPring the list of values:")
for i in values_list:
    print(i,end=" ")