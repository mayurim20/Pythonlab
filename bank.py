class bank:
    def __init__(self):
        self.balance=0
        self.accountno=int(input("enter account no:"))
        self.name=input("enter name:")
        self.accounttype=input("enter account type:")

    def display(self):
        print("name:",self.name)
        print("account number",self.accountno)
        print("account type",self.accounttype)

    def deposit(self):
        amount=int(input("enter the amount to deposite:"))
        self.balance+=amount
        print("your balance is",self.balance)

    def withdraw(self):
        amount=int(input("enter the amount to withdraw:"))
        if(amount>self.balance):
            print("insufficient balance")
        else:
            self.balance-=amount
            print("your remaining balance is:",self.balance)

account=bank()
account.display()
account.deposit()
account.withdraw()
