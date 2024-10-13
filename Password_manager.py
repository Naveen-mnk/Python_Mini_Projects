
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)   '''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

password = input("Enter master password: ")
key  = load_key()
fer  = Fernet(key)

def view():
    with open("passwords.txt","r") as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, passw = data.split("|")
            print("Account Name:", user,"| Password:",fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name +"|"+ fer.encrypt(pwd.encode()).decode() + "\n")
        print("Account and password saved Successfully!")

while True:
    option = input("Do you want to Add or View or remove ? (Add/View/Remove) or q to quit: ").lower()
    if option == "q":
        break
    if option == "view":
        view()
    elif option == "add":
        add()
    else:
        print("Invalid option!")
        continue