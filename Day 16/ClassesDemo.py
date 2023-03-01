# Introduction to OOP


# Concept: Create a Class with attributes
class MyFirstClass:
    print("Who wrote this ?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(f"{philosopher} wrote the book: {book}")


# Concept: Instance Methods
class Payment:
    def __init__(self, name, payment, amount):
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "Yes"

    def status(self):
        if self.payment == "Yes":
            return f"{self.name} is paid {str(self.amount)}"
        else:
            return f"{self.name} is not paid yet"


# Concept: Inheritance(Parent and Child Class)

# parent class
class Employee:
    def __init__(self, name, last):
        self.name = name
        self.name = last
# Child Class
class SuperVisor(Employee):
    def __init__(self,name, last, password):
        super().__init__(name, last)
        self.password = password
class Chefs(Employee):
    def leave_request(self,days):
        return f"May I take a leave for {days} days"



# Instance of MyfirstClass
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")

# Instances of Class Payment
nathan = Payment("Nathan", "No", 1000)
roger = Payment("Roger", "No", 3000)
print(nathan.status(), "\n", roger.status())
roger.pay()
print(nathan.status(), "\n", roger.status())

# Instances of Classes defined in concept: Inheritance
adrian = SuperVisor("Adrain" ,"A" ,"apple")
emily = Chefs("Emily" , "E")
juno = Chefs("Juno","J")

print((emily.leave_request(3)))
print(adrian.password)
print(emily.name)






