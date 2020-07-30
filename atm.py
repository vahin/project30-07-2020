# Vahin Sharma
accountMoney = {}
class AtmAccount(object):
    def __init__(self, accountName, accountID, balance):
        self.accountName = accountName
        self.accountID = accountID
        self.balance = balance
        accountMoney[self.accountID] = self.balance
    def deposit(self, amount):
        self.balance += amount
        accountMoney[self.accountID] = self.balance
    def withdraw(self, amount):
        if(amount > self.balance):
            print("Can't withdraw more than avaliable")
        else:
            self.balance -= amount
            accountMoney[self.accountID] = self.balance
    def transfer(self, other, amount):
        # other is the accountID
        if(amount > self.balance):
            print("Can't transfer more than available")
        else:
            accountMoney[other] += amount
            self.balance -= amount
            accountMoney[self.accountID] = self.balance

john = AtmAccount("John", 12345, 1000)
anson = AtmAccount("Anson", 23456, 12500)
anson.deposit(200)
john.transfer(23456, 20)
print("John's Balance: {} \n\nAnson's Balance: {}".format(john.balance, anson.balance))
