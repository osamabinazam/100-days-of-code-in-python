#Looping through numbers from 1 to 100 using while loop

print("Start...")
count=0
while count<=100:
    print(count)
    count = count+1
print("End....")

# Poping out list of item from a list
print("Example 2: Poping out elemnet from a list")

list = ["Maths" , "Chemistry" , "Biology" , "Urdu" , "History" , "Computer Science"]
print("List is : " , list)
print("\nPoped out elements: ")

while list:
    print(list.pop())
print( "\nList is : ",list)