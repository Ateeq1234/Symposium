print("Project-11")
print("_"*15)
class Account:
    def __init__(self,name,balance,min_balance):
        self.name= name
        self.balance= balance
        self.min_balance= min_balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance- amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry You don't have enough balance")

    def statement(self):
        print(f"Account Balance is Rs.{self.balance}")

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance,min_balance= -1000)

    def __str__(self) -> str:
        return "{}'s Current Account: Balance Rs{}".format(self.name,self.balance)


class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance,min_balance=0)

    def __str__(self) -> str:
        return "{}'s Savings Account: Balance Rs{}".format(self.name,self.balance)

x= Current("Ateeq",500)
print(x)

x1= Savings("Khalid",5000)
print(x1)
# x.deposit(300)
# print(x.withdraw(1000))
# x.statement()
# print(x.withdraw(1000))
