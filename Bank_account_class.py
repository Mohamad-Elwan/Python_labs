class Bank:
    def __init__(self, accountNumber, customerName, balance):
        self.account_Number = accountNumber
        self.customer_Name = customerName
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
         self.balance -= amount

    def display(self):
        print("Account Number:\n", self.account_Number, "\nCustomer Name:\n", self.customer_Name, "\nBalance:\n", self.balance)

bank = Bank(903182, "Mohamad Elwan", 2400)
bank.deposit(903)
bank.withdraw(182)
bank.display()