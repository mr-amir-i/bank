from services.bank_service import BankService
from utils.exceptions import (
    InvalidAmountError,
    AccountNotFoundError,
    InsufficientBalanceError,
    IncorrectPasswordError
)
bank = BankService()

START_MENU = """
    1. Login        2. Create Account
"""

MENU = """
    1. Withdraw Money       2. Deposit Money
    3. view Balance         4. Exit
"""

OPTION ={
    "1": bank.withdraw,
    "2": bank.deposit,
    "3": bank.get_balance
}

account = None
while account is None:
    print(START_MENU)
    start_choice = input("Enter your choice: ")

    try:
        if start_choice == "1":
            account_id = int(input("Enter your Account ID: "))
            password = int(input("Enter your Password: "))
            account = bank.login(account_id, password)

        elif start_choice == "2":
            name = input("Enter your Name: ")
            user_id = int(input("Enter your User ID: "))
            password = int(input("Enter your Password: "))
            account = bank.create_account(name, user_id, password)
            print(f"Account created. your account id: {account["account_id"]}")
        else:
            print("invalid choice")
    except(ValueError, TypeError,
           AccountNotFoundError,IncorrectPasswordError) as error:
        print(error)

while True:
    print(MENU)
    choice = input("Enter your choice: ")

    if choice == "4":
        print("Thank you for testing the project")
        break
    if choice not in OPTION:
        print("Invalid Choice")
        continue

    method = OPTION[choice]

    try:
        if choice in ("1", "2"):
            amount = int(input("please enter amount: "))
            balance = method(account["cart_number"], amount)
        else:
            balance = method(account["user_id"])

        print("Balance: ", balance)
    except (InvalidAmountError,
            InsufficientBalanceError,
            AccountNotFoundError,
            ValueError) as error:
        print(error)

