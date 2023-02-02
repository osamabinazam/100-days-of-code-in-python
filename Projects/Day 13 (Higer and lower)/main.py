from art import logo,vs
from Game_Data import data
import  random

# get random account from Game data for comparison
def get_random_account():
    return random.choice(data)

# Formating account into printable format
def format_account(account):
    name  = account["name"]
    description = account["description"]
    country = account["country"]
    return f"Name: {name}, a {description}, from {country}"





print(logo)

account_a = get_random_account()
account_b = get_random_account()
if account_a == account_b:
    account_b = get_random_account()

print(f"Compare A: {format_account(account_a)}")
print(vs)

print(f"Against B: {format_account(account_b)}")

input(f"\nWho has more followers? Type A or B : ")


