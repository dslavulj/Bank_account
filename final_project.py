class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def getbalance(self):
        return self.__balance
    def deposit(self,num):
        self.__balance += num
    def withdraw(self,num):
        if num > self.__balance:
            print("Inefficient funds")
        else:
            self.__balance -= num
    def transfer(self,to,num):
        if num <= self.__balance:
            self.withdraw(num)
            to.deposit(num)
            print("Transferred $ {} into your savings account.".format(num))
        else:
            print("Inefficient funds")

class SavingAccount(BankAccount):
    def __init__(self,balance):
        BankAccount.__init__(self,balance)
        
class CheckingAccount(BankAccount):
    def __init__(self,balance):
        BankAccount.__init__(self,balance)

def main():
    Saving_Account = SavingAccount(100)
    Checking_Account = CheckingAccount(500)

    print("Savings account balance: $ {}".format(Saving_Account.getbalance()))
    print("Checking account balance: $ {}".format(Checking_Account.getbalance()))

    Checking_Account.transfer(Saving_Account,100)

    print("Savings account balance: $ {}".format(Saving_Account.getbalance()))
    print("Checking account balance: $ {}".format(Checking_Account.getbalance()))

if __name__ == "__main__":
    main()
