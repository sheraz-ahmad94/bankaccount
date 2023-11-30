from bankaccount import BankAccount
import json
import random
import hashlib

bank_account_list = []

def generate_unique_number():
    digits = [i for i in range(10)]
    random.shuffle(digits)
    unique_number = ''.join(map(str, digits[:7]))

    return unique_number

def hash_password(password):
    
    password_bytes = password.encode('utf-8')

    sha256_hash = hashlib.sha256()

    sha256_hash.update(password_bytes)

    hashed_password = sha256_hash.hexdigest()

    return hashed_password

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def print_menu_user():
    print("-- MENU --")
    print("1 - Sign Up")
    print("2 - Login")
    print("3 - Exit")

def print_menu_actions():
    print("-- OPTIONS --")
    print("1 - Check Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Check Transaction History")
    print("5 - Logout")

def create_new_user(data):
    password = input("Please Enter a Secure Password: ")
    re_enter_password = input("Re-Enter the Password: ")
    if password == re_enter_password:
        account_number = generate_unique_number()
        if account_number in accounts_list:
            print("Account Exists")
        else:
            balance = int(input("Initial Deposit = "))
            password = hash_password(password)
            bank_account_list.append(BankAccount.new_user_signup(account_number, password, data, balance))

        return account_number
    else:
        return False

def extract_account_numbers(data):
    list_of_accounts = []
    for key in data:
        list_of_accounts.append(key)
    
    return list_of_accounts
            

data = load_json_file("accounts.json")
accounts_list = extract_account_numbers(data)

while True:
    print_menu_user()
    option = int(input("Select: "))

    if option == 1:
        new_account_number = create_new_user(data)
        if not new_account_number:
            print("Your Passwords do not match! Try Again!")
        else:
            print("New Account Has Been Created Successfully!")
            print(f"Your New Account Number: {new_account_number}")
            

    elif option == 2:
        accounts_list = extract_account_numbers(data)
        login_account = input("Enter Your Account Number: ")

        if login_account not in accounts_list:
            print("Account Not Found! Please Try Again!")
        else:
            password = input("Enter Password: ")
            hashed_password = hash_password(password)
            if not hashed_password == data[login_account]['hashed_password']:
                print("Password Doesn't Match! Try Again")
            else:
                print("Login Successful!")
                user_session = BankAccount(login_account, hashed_password, data, data[login_account]['balance'])
                
        while True:
            
            print_menu_actions()
            try:
                choice = int(input("Select: "))
            except ValueError as ve:
                print("Error: Invalid input. Please enter a number.")
            
            if choice == 1:
                print(f"Your Balance is: {user_session.balance}")

            elif choice == 2:
                amount = int(input("Enter the amount you want to deposit: "))
                user_session.deposit(amount)
                print(f"Amount Credited Successfully! Your new Balance is {user_session.balance} Rs.")
            
            elif choice == 3: 
                amount = int(input("Enter the amount you want to withdraw: "))
                if(user_session.withdraw(amount)):
                    print(f"Withdrawal Successfull! Remaining Amount: {user_session.balance} Rs.")
            
            elif choice == 4:
                print("- Transaction History -")
                for transaction in data[login_account]["transaction_history"]:
                    print(transaction)

            elif choice == 5:
                print("Logged Out")
                break
            else: 
                print("Wrong Choice! Select Again.")
    elif option == 3:
        break
    else:
        print("Wrong Input! Try Again. Enter a Valid Option.")