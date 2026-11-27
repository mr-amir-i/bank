# Bank Project

A command-line banking application written in Python. It supports account creation, login, deposits, withdrawals and balance checks, with all data stored in a JSON file.

## Features

### Account Creation
Create a new account with a name, user ID and password. Each account gets an auto-generated account ID and a unique card number starting with `6037`. New accounts start with a balance of 0.

### Login
Log in using your account ID and password. Wrong account IDs or passwords are rejected with a clear error message.

### Deposit
Add money to your account. The amount must be a positive number.

### Withdraw
Take money out of your account. The app blocks withdrawals larger than your current balance, and the amount must be a positive number.

### View Balance
Check your current balance at any time.

### Error Handling
The app uses custom exceptions for each failure case:
- `InvalidAmountError`: zero or negative amounts
- `InsufficientBalanceError`: not enough balance
- `AccountNotFoundError`: unknown account
- `IncorrectPasswordError`: wrong password

Invalid input, such as letters instead of numbers, is also handled without crashing the program.

### Data Persistence
All accounts are saved to `data/accounts.json` after every change, so your data is still there the next time you run the program.

## Project Structure

```
bank/
├── data/
│   └── accounts.json
├── services/
│   └── bank_service.py
├── utils/
│   └── exceptions.py
└── main.py
```

- `main.py`: menu and user interaction
- `services/bank_service.py`: banking logic (accounts, deposit, withdraw, balance)
- `utils/exceptions.py`: custom exception classes
- `data/accounts.json`: stored account data

## How to Run

```bash
python main.py
```

## Requirements

- Python 3.8+