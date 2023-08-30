class BankAccount:
# Constructor to initialize a BankAccount.
    def __init__(self, account_num, account_holder):
        self.account_num = account_num  
        self.account_holder = account_holder  
        self.balance = 0.0
    #assigning date of account opening
        from datetime import date  
        today = date.today()
        self.date = today


# Method to deposit funds into the account.
    def deposit(self, amount):
    # Ensure the deposit amount is not 0.
        if amount > 0:  
            self.balance += amount  
            print("Succesful Deposit")
            print("Avl. Amount : ", self.balance)
            print('\n')

# Method to withdraw funds from the account.
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount 
            return True 
        return False  

#Method to print balance.
    def get_balance(self):
        print("Avl. Balance : ",self.balance)
        print('\n')  

class SavingsAccount(BankAccount):
#Initialize a SavingsAccount instance, inheriting from BankAccount.
    def __init__(self, account_num, account_holder):
        super().__init__(account_num, account_holder)

        from datetime import date  
        today = date.today()
        if (self.date > today):
            self.interest_rate = 0.02  # Set the default interest rate.

# Method to apply interest to the account balance.
    def apply_interest(self):  
        self.balance = self.balance + self.balance*0.02  # Add interest to the balance.

class CurrentAccount(BankAccount):
#Initialize a CurrentAccount instance, inheriting from BankAccount.
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        


# dictionary to store account details.
accounts = {}  

while True:
    print("Banking Operations Available")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Fund transfer")
    print("5. Balance Inquiry")
    print("6. Exit")
    
    choice = input("Enter your choice: ")    

# Create a new account based on user input and add it to the accounts dictionary.
    if choice == "1":
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder name: ")
        account_type = input("Enter account type (Savings or Current): ").lower()
        if account_type == "savings":
            accounts[account_number] = SavingsAccount(account_number, account_holder)
            print("Saving Account Created")
            print('\n')
        elif account_type == "current":
            accounts[account_number] = CurrentAccount(account_number, account_holder)
            print("Current Account Created")
            print('\n')
        else:
            print("Choose Appropriate Options")
            print('\n')

# Deposit money into an existing account based on user input.
    elif choice == "2":
        account_number = input("Enter account number: ")
        if account_number in accounts:
            amount = float(input("Enter deposit amount: "))
            accounts[account_number].deposit(amount)
        else:
            print("Invalid account")
            print('\n')

# Withdraw money from an existing account based on user input.
    elif choice == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        if account_number in accounts:
            account = accounts[account_number]  # Get the account instance
            if isinstance(account, CurrentAccount):
        # If it's a CurrentAccount withdrawal charges applicable
                amount = amount+60
                print("rs.60 is charged for withdrawal")
                if account.withdraw(amount):
                    print("Withdrawal successful.")
                    print('\n')
                else:
                    print("Invalid withdrawal amount")
                    print('\n')
            else:
        # For SavingsAccount, perform a normal withdrawal.
                if account.withdraw(amount):
                    print("Withdrawal successful.")
                    print('\n')
                else:
                    print("Invalid withdrawal amount")
                    print('\n')
        else:
            print("Invalid account.")
            print('\n')


# Transfer funds between two existing accounts based on user input.        
    elif choice == "4":
        from_account_number = input("Enter your account number: ")
        to_account_number = input("Enter recipient's account number: ")
        amount = float(input("Enter transfer amount: "))
            
        if from_account_number in accounts and to_account_number in accounts:
            from_account = accounts[from_account_number]
            to_account = accounts[to_account_number]
                
            if from_account.withdraw(amount):
                print("Transfer successful.")
                to_account.deposit(amount)
                print('\n')
                
            else:
                print("Transfer failed due to insufficient balance.")
                print('\n')
        else:
            print("Invalid account(s).")
            print('\n')


# Check and display the balance of an existing account.
    elif choice == "5":
        account_number = input("Enter account number: ")
        if account_number in accounts:
            accounts[account_number].get_balance()
        else:
            print("Invalid account.")
            print('\n')


#Exit the operations
    elif choice == "6":
        print("Exiting the program.")
        break

