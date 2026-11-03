class Account():
    def __init__(self, firstname, lastn, nr, balance = 0):
        self.firstname = firstname
        self.lastn = lastn
        self.balance = balance
        self.kontoNummer = nr
        
    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount 
        else :
            print(amount)
    
    def withdrow(self, amount):
        if 0 < amount <= self.balance :
            self.balance -= amount
        else :
            print(amount)
    def __str__(self):
        return f"Счет {self.kontoNummer} ({self.firstname} {self.lastn}) - Баланс: {self.balance}"
    
acc = Account(firstname = "Jane", lastn = "Litvintsava", nr="505", balance=1000 )
print(acc)
acc.withdrow(50)
print(acc)
