
# creating first dictionary keys  between 1 and 16 with the value of square of key
# creating second dictionary keys  between 16 and 21 with the value of cube of key
square_value = {}
cubic_values = {}
for i in range(1,16):
    square_value[i] = pow(i,2)

for i in range(16,21):
    cubic_values[i] = i*i*i
print("Square Values are : ",square_value)
print("Cubic Values are  :",cubic_values)


# Merging using copy and update methods
# During merging of the dictionaries
# so only one pair of key and values is store in the dictionary
# because duplicate keys are not allowed
merge_value ={}
merge_value=square_value.copy()
merge_value.update(cubic_values)
print("Merged Dictionary Using Built-in Functions is : \n",merge_value)

# Merging two dictionary into one
merged_value = {}
for key in square_value:
    merged_value[key] = square_value[key]
for key in cubic_values:
    merged_value[key] = cubic_values[key]
print("\nMerged Dictionary Using Loop is : \n",merged_value)

