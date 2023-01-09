# Calculating the sum of integer items of the dictionary
def sum(dictionary):
    sum=0;
    for key,value in dictionary.items():
        sum += value
    return  sum

# Calulating the average of disctionary items
def average(dictionary):
    sum=0;
    for key,value in dictionary.items():
        sum += value
    return  sum/len(dictionary)

# Calculating the mean of the dictionary items
def mean(dictionary):
    sum=0;
    for key,value in dictionary.items():
        sum += value
    return  sum/len(dictionary)
# Perform summation on string
def sum_of_string (dictionary):
    sum="";
    for key,value in dictionary.items():
        sum += value
    return  sum

# Calculaing the product of string items (concatenate strings)of the dictionary
def product(dictionary):
    product=1
    for key,value in dictionary.items():
        product*=value
    return  product

# Calculaing the product of string values of the dictionary
def product_of_string(dictionary):
    product=""
    for key,value in dictionary.items():
        product*=str(value)
    return  product

dict_1 = {
    1:45.5,
    2: 44.5
}
dict_2 ={
    1: 45,
    2: 50
}
dict_3 ={
    1: "Hello",
    2: "World"
}
print("Sum of values of dict 1 is : ",sum(dict_1))
print("Sum of values of dict 2 is : ",sum(dict_2))
print("Sum of values of dict 3 is : ",sum_of_string(dict_3))
print("Product of values of dict 1 is : ",product(dict_1))
print("Product of values of dict 2 is : ",product(dict_2))

# print("Product of values of dict 3 is : ",product_of_string(dict_3))
print("Average of values of dict 1 is : ",average(dict_1))
print("Average of values of dict 2 is : ",average(dict_2))
# print("Average of values of dict 3 is : ",average(dict_3))
print("Mean of values of dict 1 is : ",mean(dict_1))
print("Mean of values of dict 2 is : ",mean(dict_2))
