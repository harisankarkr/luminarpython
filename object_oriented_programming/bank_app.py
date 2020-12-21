class bank:
    bank_name="HDFC"
    def __init__(self,acno,person_name,balance):
        self.acno=acno
        self.person_name=person_name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("your",bank.bank_name, "account ",self.acno," has been credited with amount of",amount," your avalilable balance is ",self.balance)

    def withdraw(self,amount):
        self.amount=amount
        if(amount>self.amount):
            print("insufficient amount in your account transaction failed")
        else:
            self.balance-=amount
            print("your account ",self.acno," has been debited with amount ",amount," you avl balance ",self.balance)

    def balance_enq(self):
        print("you current account balance is",self.balance)

obj=bank(2412,"hari",2800)
obj.deposit(5000)
#obj.withdraw(3200)
#obj.balance_enq()
#print(obj.acno)
