
import Cipher_art
from Ceaser_Cipher import encrypt,decrypt
def menu():
    while True:
        print("***************************************")
        print("****            Menu               ****")
        print("***************************************\n")
        print("1. Encrypt ")
        print("2. Decrypt ")
        print("3. Exit")
        menu_choice = int(input("Enter your choice: "))
        if menu_choice == 1:
            message = input("Enter message: ")
            key = int(input("Enter key: "))
            encrypt(message,key)
        elif menu_choice == 2:
            message = input("Enter message: ")
            key = int (input("Enter key: "))
            decrypt(message,key)
        elif menu_choice == 3:
            exit(0)
        print("Wanna use menu again? ")
        if input("Press (Y/y) key to continue: ") in ['y','Y']:
            continue
        else:
            print("Exiting...")
            exit(0)
if __name__ == "__main__":
    print(Cipher_art.logo)
    menu()
