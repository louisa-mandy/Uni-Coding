from bank1 import Account
from bank1 import Customer
from bank1 import Bank 

bank = Bank("BCA")

#creating a customer

bank.addCustomer("Michelle", "Sandrica")
bank.addCustomer("Louisa", "Mandy")
bank.addCustomer("Lee", "Heesung")
bank.addCustomer("Leon", "Kennedy")

print(bank.getCustomer(0).getFirstName())
print(bank.getNumOfCustomers())













#for printing customers names 

from bank1 import Account
from bank1 import Customer

customer1 = Customer("Louisa","Mandy",100000000000000000)

print(customer1.getFirstName())
print(customer1.getLastName())



print(customer1.getAccount())



#for showing the result of balance / depositing 

acc1 = Account(15000)

print("creating an account with")
print(f"{acc1.getBalance()} balances")

if acc1.deposit(3000):
    print("Deposit Succesfull")
    print(f"Balance: {acc1.getBalance()}")
else:
    print("Deposit Failed")
    print(f"Balance: {acc1.getBalance()}")

if acc1.withdraw(1000):
    print("Withdrawal Succesfull")
    print(f"Balance: {acc1.getBalance()}")
else:
    print("Withdrawal Failed")
    print(f"Balance: {acc1.getBalance()}")


