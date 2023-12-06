"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, payType, pay, hours, contracts, contractPay, bonusPay):
        self.name = name
        self.payType = payType
        self.totalPay = 0
        self.pay = pay
        self.hours = hours
        self.contracts = contracts
        self.contractPay = contractPay
        self.bonusPay = bonusPay
        if(self.payType == "Salary"):
            self.totalPay += self.pay
        else:
            self.totalPay += (self.pay * self.hours)
        if(self.contracts > 0):
            self.totalPay += (self.contracts * self.contractPay)
        self.totalPay += self.bonusPay

    def get_pay(self):
        return self.totalPay

    def __str__(self):
        retString = ""
        if (self.payType == "Salary"):
            retString += (self.name + " works on a monthly salary of " + str(self.pay))
        else:
            retString += (self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.pay) + "/hour")
        if (self.contracts > 0):
            retString += (" and receives a commission for " + str(self.contracts) + " contract(s) at " + str(self.contractPay) + "/contract.")
        elif (self.bonusPay > 0):
            retString += (" and receives a bonus commission of " + str(self.bonusPay) + ".")
        else:
            retString += (".")
        retString += (" Their total pay is " + str(self.totalPay) + ".")
        return retString

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
