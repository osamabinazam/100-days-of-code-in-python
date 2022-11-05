# Loop in Python
# Topics covered : for loop , range() in loop
# Day 5 of 100 Days of Code


print("\nTopic : for loop:\n")
# Implementing a simple loop
# Whenever colon is used indentation is mandatory
fruits = ["Apples", "Bananas", "Guava", "Peace", "Pear"]
for fruit in fruits:
    print(fruit,fruit + " Pie")
# Outside the loop
print(fruits)

print("\nExercise 5.1:")
# Exercise 5.1:
# Calculate the average height from the given list of heights of the students
students_height = [180,124,165,173,189,169,146]
# print ("The length of the list is : " , len(students_height))
print("Heights : " , students_height)
sumofheights =0;
average=0;
for height in students_height:
    sumofheights+=height;
average = sumofheights / len(students_height)
print("Average Height is : ", average)


# Calculating the average height by getting list from the user
# students_height = input("Enter the list of heights: ").split()
# for n in range(0,len(students_height)):
#     students_height[n] = int (students_height[n])
# print(students_height)
# # calculating Average using builtin functions
# average = sum(students_height) / len(students_height)
# print("Average Height is : ", average)

print("\nExercise 5.2:")
# Exercise 5.2:
# Higest Score Exercise
score = [60,94,88,56,50,55,40]
print("Scores : ",score)
# Calculating Maximum marks
highest=0
for i in score:
    if i >= highest:
        highest = i;
print("Highest score is : " , highest)

# Topic : range() in loop
# Printing number from 1 to 10 using range()
# 10 will not be included in the range
print("\nTopic : range() in for loop")
print("Printing numbers from 1 to 9:")
for number in range(1,10):
    print(number)




