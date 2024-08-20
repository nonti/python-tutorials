# Python Encapsulation Challenge

# 1. Create 'BankAccount' class with private attributes and methods.
class BankAccount:
    def __init__(self, initial_balance: float, account_number: str):
        self.__account_balance = initial_balance
        self.__account_number = account_number
        
    def deposit(self, amount):
        if amount > 0 :
            self.__account_balance += amount
        else:
            print('Deposit amount must be positive.')
        
    def withdraw(self, amount: float):
        if amount > 0:
            self.__account_balance -= amount
        else:
            print('Insufficient finr for withdrawal amount')
    
    def get_balance(self):
        return self.__account_balance
    

account = BankAccount(1000.0, '123456789')
    
account.deposit(500.0)
print('Balance after desposit: ',account.get_balance())
account.withdraw(200.0)
print(f'Balance after withdrawal: ', account.get_balance())
    
    
    