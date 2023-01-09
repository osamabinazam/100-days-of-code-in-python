
dict_1 = {
    1:200,
    2:400,
    3:600,
    4:550
}

dict_2 ={
    3:100,
    5:200,
    1:100,
    6:200
}

# adding common keys values to make them a single value

# Getting key and values of dictionary 1
keys1 = list(dict_1.keys())
values1 = dict_1.values()

# getting key and values of dictionary 2
keys2=dict_2.keys()
values2=dict_2.values()

# Getting the lengths of the dictionary
len1 = len(keys1)
len2 = len(keys2)
max_len = max(len1,len2)
# print("Max length is : ",max_len)

# Now check duplications and remove them
temp_dict ={}
for i in keys1:
    for j in keys2:
        if i == j:
            dict_1[i] = (dict_1.get(i) + dict_2.get(j))

# now coping two list into one so that we can remove duplicates
temp_dict = dict_2.copy()
temp_dict.update(dict_1)
new_dict ={}
del keys1,keys2,dict_1,dict_2   # deleting unneccesary lists and dictionaries from memory

# Sorting dictionary using keys and list
keys = list(temp_dict.keys())
keys.sort()
for i in keys:
    new_dict[i] = temp_dict.get(i)

del keys
print("New Dictionary is : ",new_dict)