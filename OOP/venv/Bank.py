
class Bank:
    def __init__(self):
        self.accounts = []


class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust


class Costumer:
    def __init__(self, name):
        self.name = name


b = Bank()
c = Costumer('Claus')
b.accounts.append(Account(1234, c))
print(b.accounts[0])
