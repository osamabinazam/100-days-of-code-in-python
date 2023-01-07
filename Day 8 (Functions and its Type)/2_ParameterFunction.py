def greetWithName(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")
    print("Isn't weather nice today ?")

# Function used to calculate the Body Mass index
# A BMI below 18.5 is considered underweight.
# A BMI of 18.5 to 24.9  is considered healthy.
# A BMI of 25 to 29.9  is considered overweight.
# A BMI of 30 to 39.9 is considered obese.
def bmi (height , weight ):
    bmi = (weight/(height**2))
    if bmi < 18.5:
        print('Underweight')
    if bmi >= 18.5 and bmi < 25:
        print("Normal")
    if bmi  >= 25 and bmi < 30:
        print('Overweight')
    if bmi >= 30:
        print('Obesity')

#Calling Function
greetWithName("Osama")

# Calculating BMI
height = float (input("Input height : "))
weight = float (input("Input weight : "))
bmi(height ,weight)
