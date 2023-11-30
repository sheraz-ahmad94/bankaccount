import json
import datetime

class BankAccount:
    all = []
    def __init__(self, account_number, password, data = 0, balance = 0) -> None:
        self.__account_number = account_number
        self.__password = password
        self.__balance = balance
        self.transaction_history = []
        self.data = data

    @property
    def balance(self):
        return self.__balance
    
    @property
    def account_number(self):
        return self.__account_number
    
    @account_number.setter
    def account_number(self, value):
        self.__account_number = value
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        self.__password = value
    
    @balance.setter
    def balance(self, value: int):
        self.__balance = value
    
    def withdraw(self, amount: int):
        if(amount > self.__balance):
            print("Balance Low! Balance cannot be negative.")
        else:
            self.__balance = self.__balance - amount
            
            new_transaction = {
                "transaction_type": "Withdraw",
                "amount": amount,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            self.data[str(self.account_number)]["balance"] = self.balance
            self.data[str(self.account_number)]["transaction_history"].append(new_transaction)

            file_path = "accounts.json"

            with open(file_path, "w") as json_file:
                json.dump(self.data, json_file, indent=4)

            return True

        
    def deposit(self, amount: int):
        new_balance = self.__balance + amount
        self.__balance = new_balance

        
        new_transaction = {
            "transaction_type": "Deposit",
            "amount": amount,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        

        self.data[str(self.account_number)]["balance"] = new_balance
        self.data[str(self.account_number)]["transaction_history"].append(new_transaction)

        file_path = "accounts.json"

        with open(file_path, "w") as json_file:
            json.dump(self.data, json_file, indent=4) 

    
    @classmethod
    def new_user_signup(cls, account_number, password, data, balance = 0):
        BankAccount(
            account_number = account_number,
            password = password,
            balance = balance,
            data = data
        )

        user = {}
        user[account_number] = {}
        user[account_number]["hashed_password"] = password
        user[account_number]["balance"] = balance
        user[account_number]["transaction_history"] = []

        file_path = "accounts.json"

        existing_data = data
        
        existing_data.update(user)

        with open(file_path, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)

