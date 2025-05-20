class Bank:
    bank_name = "Default Bank" 

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


customer1 = Bank("Alice")
customer2 = Bank("Bob")

print(f"{customer1.customer_name} - Bank: {customer1.bank_name}")
print(f"{customer2.customer_name} - Bank: {customer2.bank_name}")

Bank.change_bank_name("New Generation Bank")

print(f"{customer1.customer_name} - Bank: {customer1.bank_name}")
print(f"{customer2.customer_name} - Bank: {customer2.bank_name}")
