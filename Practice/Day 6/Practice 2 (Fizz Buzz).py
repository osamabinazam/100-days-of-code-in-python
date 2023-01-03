
# Multiple of
def ismultipleOf(nominator,denominator):
    if int(nominator) % int(denominator) == 0:
        return True
    else:
        return False
#FizzBuzz function definition
def fizz_buzz(startFrom, endAt):
    startFrom = int(startFrom)
    while startFrom <= int(endAt):
        if ismultipleOf(startFrom,3) and ismultipleOf(startFrom,5):
            print("FizzBuzz")
        elif ismultipleOf(startFrom,3):
            print("Fizz")
        elif ismultipleOf(startFrom,5):
            print("Buzz")
        print(startFrom)
        startFrom = startFrom+1

#Driver for Fizz Buzz
#Range
startFrom = input("Input starting number : " )
endAt = input("Input ending number : " )
#Calling FizzBuzz
fizz_buzz(startFrom,endAt)
