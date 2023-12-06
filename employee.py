"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary_type, salary, working_time, commission_type, commission, contract_number):
        self.working_time = working_time   
        self.contract_number = contract_number
        self.commission = commission
        self.commission_type = commission_type
        self.salary_type = salary_type
        self.name = name
        self.salary = salary

    def get_pay(self):
        no_commission = 0
        with_commission = 0
        if self.salary_type == "monthly":
            no_commission = int(self.salary)
        elif self.salary_type == "hourly":
            no_commission = int(self.salary) * int(self.working_time)
        else:
            print("sth wrong with salary_type")
        if self.commission_type == "no":
            return no_commission
        elif self.commission_type == "fixed":
            with_commission = int(self.commission) + no_commission
            return with_commission
        elif self.commission_type == "flexible":
            with_commission = (int(self.commission) * int(self.contract_number)) + no_commission
            return with_commission
        else:
            print("sth wrong with commission_type")

    def __str__(self):
        if self.salary_type == "monthly":
            if self.commission_type == "no":
                return self.name + " works on a " + self.salary_type + " salary of " + str(self.salary) + ". " + "Their total pay is " + str(self.get_pay()) + "."
            elif self.commission_type == "fixed":
                return self.name + " works on a " + self.salary_type + " salary of " + str(self.salary) + " and receives a bonus commission of " + str(self.commission) + ". "  + "Their total pay is " + str(self.get_pay()) + "."
            elif self.commission_type == 'flexible':
                return self.name + " works on a " + self.salary_type + " salary of " + str(self.salary) + " and receives a commission for " + str(self.contract_number) + " contract(s) at " + str(self.commission) + "/contract" + ". "  + "Their total pay is " + str(self.get_pay()) + "."
        elif self.salary_type == "hourly":
            if self.commission_type == "no":
                return self.name + " works on a contract of " + str(self.working_time) + " hours at " + str(self.salary) + "/hour. " + "Their total pay is " + str(self.get_pay()) + "."
            elif self.commission_type == "fixed":
                return self.name + " works on a contract of " + str(self.working_time) + " hours at " + str(self.salary) + "/hour" + " and receives a bonus commission of " + str(self.commission) + ". "  + "Their total pay is " + str(self.get_pay()) + "."
            elif self.commission_type == 'flexible':
                return self.name + " works on a contract of " + str(self.working_time) + " hours at " + str(self.salary) + "/hour" + " and receives a commission for " + str(self.contract_number) + " contract(s) at " + str(self.commission) + "/contract" + ". "  + "Their total pay is " + str(self.get_pay()) + "."



billie = Employee('Billie', 'monthly', 4000, 1, 'no', 'no', 'no')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', '25', 100, 'no', 'no', 'no')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly', 3000, 1, 'flexible', 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', 25, 150, 'flexible', 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', 2000, 1, 'fixed', 1500, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', 30, 120, 'fixed', 600, 0)
