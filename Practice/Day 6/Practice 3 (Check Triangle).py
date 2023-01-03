
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

def isIsosceles(lengths):
    if lengths[0] == lengths[1] or lengths[1] == lengths[2] or lengths[2] == lengths[0]:
        return True

def isEquilateral(lengths):
    if lengths[0] == lengths[1] == lengths[2]:
        return   True
def isScelene(lengths):
    if lengths[0] != lengths[1] != lengths[2]:
        return  True

#Main Program
lengths = []
lengths.append(input("Enter x : "))
lengths.append(input("Enter y : "))
lengths.append(input("Enter z : "))

print("Lengths are : " , lengths)

if isEquilateral(lengths):
    print("Given trianle is Equilateral.")
elif isIsosceles(lengths):
    print("Given triangle is isosceles.")
elif isScelene(lengths):
    print("Given Trianle is Scalene.")