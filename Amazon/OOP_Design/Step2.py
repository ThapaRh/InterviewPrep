'''
Lets learn about encapsulation and abstraction
'''
'''
encapsulation: 
putting all the data and methods that operate on that data on the single unit which is called class
and also restricting direct access to some components. In static programming language: it's called using access modifiers like private,protected and public
'''
#eg is a bank class, we have balance but we want to able to access that via methods only 

class Bank:
    def __init__(self,balance):
        self._balance = balance #_balance means balance is private(just a way to express in python, it doesnot make that attribute private but if we waant oop behavior in python we have some rules and _ is one of that)
    
    def deposit(self,amount):
        self._balance+=amount
        
    def get_balance(self): 
        return self._balance
    
    #this is encapsulation, control how the object is used
    
'''
abstraction: 
hiding the complex implemenation details and showing only what's needed
'''
class CoffeeMachine():
    def brew_coffee(self):
        self._boil_water()
        self._grind_beans()
        print("serving coffee")
        
    def _boil_water(self): #private method
        print("water is boiling")
    
    def _grind_beans(self):
        print("grinding_beans")
        
        #here we hid unnecessary details of coffee making and only showed whats needed to user