import math


# Add two numbers
def add(number1 , number2 ):
    return  number1+number2

# Subtract two numbers
def subtract(number1, number2 ):
    return number1-number2

# Multiply two numbers
def multiply(number1, number2):
    return number1*number2

# Divide two numbers
def divide(number1, number2):
    return number1/number2

# Calculate the square root of a number
def sqrt(number):
    return math.sqrt(number)

# Calculate the cube root of a number
def cube(number):
    return math.pow(number, 3)
# Storing function into dictionary with assiciated operator as a key
operation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '√': sqrt,
    'c': cube
}
operator=''
#Menu
while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square Root\n6. Cube Root\n7. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        operator='+'
        break
    elif choice == '2':
        operator='-'
        break
    elif choice == '3':
        operator='*'
        break
    elif choice == '4':
        operator='/'
        break
    elif choice == '5':
        operator='√'
        break
    elif choice == '6':
        operator='c'
        break
    elif choice =='7':
        exit(0)



# Getting inputs
number_1 = int(input('Enter first number: '))
number_2 = int(input('Enter second number: '))

# Now when I provide operator as a key to dictionary to retrieve it's value
# from the dictionary a whole function will be retrieved
calculation_function = operation.get(operator)
answer = calculation_function(number_1,number_2)
print(f"{number_1} {operator} {number_2} = {answer}")


