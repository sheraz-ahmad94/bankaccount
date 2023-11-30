# Bank Account Program

This console-based Python program simulates a simple bank account system. It includes features such as user sign-up, login, checking balance, deposit, and withdrawal.

## Features

- **User Sign-Up:** New users can create an account with a randomly generated account number and a securely hashed password.

- **User Login:** Existing users can log in by entering their account number and password, which is hashed and compared for security.

- **Account Operations:**
  - **Check Balance:** Users can check their account balance.
  - **Deposit:** Users can deposit funds into their account.
  - **Withdrawal:** Users can withdraw funds from their account.

- **Transaction History:** The program maintains a transaction history for each user, recording deposit and withdrawal transactions.

## Usage

1. **Sign-Up:**
   - Run the program and choose the sign-up option.
   - Follow the prompts to create a new account.

2. **Login:**
   - Choose the login option and enter your account number and password.

3. **Perform Transactions:**
   - Once logged in, you can perform various transactions like checking balance, depositing, or withdrawing.

4. **View Transaction History:**
   - Users can view their transaction history to see a record of their previous transactions.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/bank-account-program.git

2. Navigate to the project directory:

   ```bash
   cd bank-account-program

3. Run the program:

   ```bash
   python main.py

## Dependencies
This program uses the following Python modules:
   - **json:** For reading and writing data to a JSON file.
   - **random:** For generating random account numbers.
   - **hashlib:** For securely hashing passwords.
