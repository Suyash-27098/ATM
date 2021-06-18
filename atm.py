class Atm(object):
    def __init__(self, cardNumber, pinNo):
        self.cardNumber = cardNumber
        self.pinNo = pinNo

    def cashWithdrawl(self, amount):
        print("Cash was Withdrawn ",amount)

    def balanceEnquiry(self):
        print("balanceEnquiry")

    def cashDeposit(self, amount):
        print("Cash was Deposited ",amount)

user = Atm(1234,4321)
print(user.cardNumber)

user.cashWithdrawl(500)
user.balanceEnquiry()
user.cashDeposit(1000)