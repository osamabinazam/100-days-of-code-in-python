# Prime numbers are numbers that can only ve divisible by 1 and itself
def prime_number(number):
    checkFlag = False
    if number==1:
        checkFlag=True
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                checkFlag=True
                break;
        if checkFlag:
            print (f"{number} is not a prime number")
        else:
            print(f"{number} is a prime number")

#Main
first = int (input("Input first number: "))
nth = int(input("Input nth number: "))
for i in range(first,nth+1):
    prime_number(i)