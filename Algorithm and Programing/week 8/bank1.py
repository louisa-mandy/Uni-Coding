#making a bank/ account/ customer 

class Account: 
    def __init__(self, init_balance=0):
        self.__balance = init_balance
    
    def getBalance(self):
        return self.__balance
    
    def deposit(self,amt):
        if amt > 0:
            self.__balance += amt 
            return True 
        return False
    
    def withdraw(self,amt):
        if amt > 0:
            self.__balance  -= amt
            return True 
        return False


class Customer: 
    def __init__(self,firstName= "", lastName= "",account=Account ):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__account = account

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName
    
    def getAccount(self):
        return self.__account

    def setAccount(self,account):
        self.__account = account

class Bank: 
    def __init__(self,bankName= ""):
        self.__bankName = bankName
        self.__customers = []
        self.__numberOfCustomers = 0     

    def addCustomer(self, firstName, lastName):
        self.__customers.append(Customer(firstName, lastName))
        self.__numberOfCustomers+=1

    def getNumOfCustomers(self):
        return self.__numberOfCustomers
    
    def getCustomer(self,index):
        return self.__customers[index]
















      
    


