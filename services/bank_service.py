import random
import json
from pathlib import Path
from utils.exceptions import InvalidAmountError, AccountNotFoundError, InsufficientBalanceError, IncorrectPasswordError


class BankService:
    def __init__(self):
        self.accounts = []
        self.file_path = Path(__file__).parent.parent / "data" / "accounts.json"
        self.load_account()

    def login(self, account_id, password):
        for account in self.accounts:
            if account["account_id"] == account_id:
                if account["password"] == password:
                    return account
                raise IncorrectPasswordError("Incorrect Password")
        raise AccountNotFoundError("Account not found")


    def save_accounts(self):
        with open(self.file_path, "w") as f:
            json.dump(self.accounts, f, indent=4)

    def generate_card_number(self):
        while True:
            cart_number = "6037" + str(random.randint(6**14,6**15-1))
            if not any(
                account["cart_number"] == cart_number
                for account in self.accounts
            ):
                return cart_number

    def create_account(self,name,user_id, password=1111, balance = 0):
        cart_number = self.generate_card_number()

        account ={
            "account_id": len(self.accounts)+1,
            "name": name,
            "user_id": user_id,
            "cart_number": cart_number,
            "password": password,
            "balance": balance
        }

        self.accounts.append(account)
        self.save_accounts()

        return account

    def load_account(self):
        try:
            with open(self.file_path, "r") as f:
                self.accounts = json.load(f)

        except FileNotFoundError:
            self.accounts = []

    def deposit(self, cart_number, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")

        for account in self.accounts:
            if account["cart_number"] == cart_number:
                account["balance"] += amount
                self.save_accounts()
                return account["balance"]
        raise AccountNotFoundError("Amount not found")

    def withdraw(self, cart_number, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")

        for account in self.accounts:
            if account["cart_number"] == cart_number:
                if account["balance"] < amount:
                    raise InsufficientBalanceError("Insufficient Balance")
                account["balance"] -= amount
                self.save_accounts()
                return account["balance"]

        raise AccountNotFoundError("Amount not found")

    def get_balance(self,user_id):

        for account in self.accounts:
            if account["user_id"] == user_id:
                    return account["balance"]

        raise AccountNotFoundError("Account not found")
