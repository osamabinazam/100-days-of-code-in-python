
# Function responsible for find a number which is divisible by n and multiple of m
def divisible_and_multiple(number, n ,  m):
    if isdivisibleBy(number,n) and ismultipleOf(number,m):
            return True
    else:
        return  False
# Divisible by
def isdivisibleBy(nominator, denominator):
    if int(nominator)%int(denominator)==0:
        return  True
    else:
        return False

# Multiple of
def ismultipleOf(nominator,denominator):
    if int(nominator) % int(denominator) == 0:
        return True
    else:
        return False


#Main Function
print("Enter a numbenr  : ")
number = input()
print("Divisible by : ")
divisibleBy = input()
print("Multiple of : ")
multipleOf =input()

#Function calling
returnedValue = divisible_and_multiple(number ,divisibleBy ,multipleOf)
if returnedValue:
    print("Yes! Number is mulipleof " + multipleOf + " and Divisible by " + divisibleBy +".")
else:
    print("No! Number is not mulipleof " + multipleOf + " and Divisible by " + divisibleBy +".")

# Function Calling
# divisible_and_multiple(num1 ,n)
