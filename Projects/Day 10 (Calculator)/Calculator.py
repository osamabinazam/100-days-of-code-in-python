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

def menu():
    # Menu
    operator = ''
    while True:
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            operator = '+'
            break
        elif choice == '2':
            operator = '-'
            break
        elif choice == '3':
            operator = '*'
            break
        elif choice == '4':
            operator = '/'
            break
        elif choice == '5':
            exit(0)
        else:
            break
    return operator

def select_op_and_num ():
    print("Select an operation for further calculation on previous answer: ")
    operator = menu()
    next_number = float(input("Enter next number: "))

    return  operator,next_number

def Main():
    logo = """
     _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """
    print(logo)


    # Storing function into dictionary with assiciated operator as a key
    operation = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }
    should_continue = True
    operator = menu()

    # Getting inputs
    number_1 = float(input('Enter first number: '))
    number_2 = float(input('Enter second number: '))

    # Now when I provide operator as a key to dictionary to retrieve it's value
    # from the dictionary a whole function will be retrieved
    calculation_function = operation.get(operator)
    answer_1= calculation_function(number_1,number_2)
    print(f"{number_1} {operator} {number_2} = {answer_1}")
    while should_continue:
        choice = input(f"Do you want to continue calculation with result {answer_1} ? Type y or Y:")
        if choice == 'y' or choice == 'Y':
            operator,next_number = select_op_and_num()
            calculation_function = operation.get(operator)
            answer_2 = calculation_function(answer_1,next_number)
            print(f"{answer_1} {operator} {next_number} = {answer_2}")
            answer_1=answer_2
        else :
            print("\nResetting calculator to fresh start")
            should_continue = False
            Main()

if __name__ == '__main__':
    Main()