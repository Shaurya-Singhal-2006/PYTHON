# create account class with 2 attributes - balance and account no.
# create methods for debit, credit and printing the balance

class account:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no
    
    def debit(self,amount):
        self.balance -= amount
        print("₹",amount,"debited from account",self.acc_no)
        print("remaining amount:",user1.balance)

    def credit(self,amount):
        self.balance += amount
        print("₹",amount,"credited to account",self.acc_no)
        print("remaining amount:",user1.balance)

user1 = account(10000,512)
print(user1.balance)
print(user1.acc_no)
print("\n")

user1.debit(5500)
print("\n")

user1.credit(2000)
print("\n")