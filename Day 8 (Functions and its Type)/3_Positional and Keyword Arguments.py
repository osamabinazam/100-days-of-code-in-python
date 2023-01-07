# Positional argument means that the argument must be provided in a
# correct position in a function call.

# With keyword arguments, the position does not matter, because a
# keyword is labeled with a keyword.
from math import  ceil
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What it is like in {location}\n")

def calculating_area (wall_height , wall_width, area_cover):
    totalarea = wall_height*wall_width
    number_of_cans = ceil ((totalarea) / (area_cover))
    print(f"Number of required to pain is(are) : {number_of_cans}" )

# Position argument
greet_with("Osama" , "Morocco")
# Keyword arguments
greet_with(location="Morocco" , name="Osama")
wheight = float(input("Input height of the wall : "))
wweidth = float(input("Input weidth of the wall : "))
coverage_of_can = float(input("Input the coverage area of one can : "))
calculating_area(area_cover=coverage_of_can,wall_width=wweidth,wall_height=wheight)

 