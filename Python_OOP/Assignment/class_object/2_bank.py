class BankAccount:

    amount_available = 500

    def deposit(self,amount):
        print(f"deposited amount is {amount}")
        self.amount_available += amount
        print(f"total amount available is {self.amount_available}")

        return self.amount_available

    def withdrawl(self,withdrawl):
        print(f"withdrawed the amount {withdrawl}")
        self.amount_available -= withdrawl
        print(f"total amount available is {self.amount_available} after withdrawl")

b1 = BankAccount()

cal = b1.deposit(200)
print(cal)
#print(b1.withdrawl(400)) 
