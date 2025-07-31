'''
| Step | What You Do                            | Why It Matters                    |
| ---- | -------------------------------------- | --------------------------------- |
| 1    | Clarify requirements                   | Build shared understanding        |
| 2    | Identify entities (nouns)              | Lay foundation for class design   |
| 3    | Define responsibilities & interactions | Model system behavior             |
| 4    | Design class skeletons                 | Show OOP skills & clean structure |
| 5    | Discuss edge cases and extensions      | Show depth & foresight            |

Design a vending machine:
Dispenses snacks and drinks
Users can insert money, choose product,get the item
if item is out of stock or not enough money is inserted the machine handles that too


Step 1: Clarify Requirements
✅ Pro-Level Clarification Checklist (Mentally Run This):
Actors – Who are the users of the system? Admin? Customer? Others?

Inputs – What are the inputs? (e.g., cash, product ID)

Outputs – What should the system respond with? (product? error? refund?)

State – What needs to be stored or tracked? (stock, money, logs)

Failure Cases – What could go wrong? (stock out, no change, payment failure)

Simplifications – Can we scope anything down? (e.g., only coins, only snacks)

Asking questions to interviewer:
    1. How does machine handle change?like extra money given by user? 
    Answer from interviewer: 
    Yes, the machine should handle change management. 
    If the user inserts more money than the product costs, the machine should return the correct change — 
    assuming it has enough change available. If not, the transaction should be rejected.
    -new requirement is added- 
    ##vending machine should handle change by keeping track of current notes and coins. Should calculate and return correct change after purchase, if not there, transation shouldnot be completed.

    2. If item is out of stock, how to handle that?
    Show an ‘Out of Stock’ message,
    Offer the user to choose another item,
    Or allow them to cancel and get a full refund.”
    
now final requirements:
- only accepts cash
- keeps track of stocks
- handles change return
- handles out of stock logic
- offers refunds if purchase can't proceed


Step 2: Identifying the entities
| Question                            | If Yes → Make It a Class |
| ----------------------------------- | ------------------------ |
| Is it a **real-world noun**?        | Likely a class           |
| Does it have **data and behavior**? | Definitely a class       |
| Do you have **many of them**?       | Needs a blueprint        |
| Will it **change or grow** later?   | Safer to isolate it      |

I identified: user,vendingmachine,moneymanager,snacks


Step 3: Define the attributes and methods of each class
🧠 How to Choose the First Entity
Use this priority:
Priority	Rule	Why It Helps
1️⃣	Start with the most concrete, self-contained entity	Easy to model, builds confidence
2️⃣	Pick something that doesn’t depend on other classes yet	Avoid circular thinking
3️⃣	Prefer data-heavy objects first	You’ll use them in other classes

I pick snack first:
And then user
| Criteria         | How You're Doing                               |
| ---------------- | ---------------------------------------------- |
| **Cohesion**     | High — class has a clear single responsibility |
| **Clarity**      | Method names reflect behavior well             |
| **Coupling**     | Low — doesn’t depend on other classes directly |
| **Completeness** | Good enough for LLD-level modeling ✅           |

'''

#this is very noobie approach, will do better next time
from datetime import date

class Snack():
    def __init__(self,name:str,brand:str,expire_date:date,cost:float):
        self.name = name
        self.brand = brand
        self.expire_date = expire_date
        self.cost = cost

    def is_fresh(self):
        return self.expire_date>date.today()
    
    def get_cost(self):
        return self.cost
    
    def get_brand(self):
        return self.brand
        
class MoneyProcessor():
    def __init__(self,t_amount):
        self.t_amount = t_amount
    
    def process_payment(self,amount:float,actual_cost:float):
        change = amount-actual_cost
        if change<0:
            #raise ValueError("Insufficient Payment")
            return {
                "message":"Insufficient funds",
                "code":400,
                "change":0
            }
        elif change>self.t_amount:
            #raise ValueError("Machine doesnot have enough change")
            return {
                "message":"Machine doesnot have enough change",
                "code":500,
                "change":0
            }
        else:
            t_amount+=actual_cost
            return {
                "message":"successful purchase",
                "code":200,
                "change":change
            }    

class VendingMachine():
    def __init__(self,money_processor):
        self.snacks = {}#list of snack objects
        self.money_processor = money_processor
    
    def purchase_snack(self,snack:str,quantity:int,money:float):
        if snack in self.snacks:
            self.update_stock(snack,quantity)
            snack_obj = self.snacks[snack]
            response = self.money_processor.process_payment(money)
            check_stock = snack_obj.check_stock(quantity)
            if check_stock and response["change"]:
                return {
                    "success" : True,
                    "change":response["change"],
                    "message":"Enjoy your snack"
                }
            elif response["message"]==400:
                return {
                    "success" : False,
                    "change":0,
                    "message":"Would you like to select different snack or add more money?"
                }
            else:
                return {
                    "success" : False,
                    "change":0,
                    "message":"No change available, would you like to buy more?"
                }
        
    def update_stock(self,snack_name,q):
        #suggested by chatu and vvimp:
        if snack_name in self.snacks:
            snack_obj,quantity = self.snacks[snack_name]
            if q>self.quantity:
                raise ValueError("Out of Stock.")
            quantity-=q
            self.snacks[snack_name]=(snack_obj,quantity)
            return True
    
    def restock(self,snack_name:str,q):
        if snack_name in self.snacks:
            snack_obj,quantity = self.snacks[snack_name]
            quantity+=q
            self.snacks[snack_name]=(snack_obj,quantity)
    
    def add_new_snacks(self,snack_name):
        #pass will add new snacks to the stock
        pass
import uuid
class User():
    def __init__(self,vending_machine:VendingMachine):
        self.id = uuid.uuid4()
        self.vending_machine = vending_machine
        
    def purchase_snack(self,snack_name,q,money):
        response = self.vending_machine.purchase_snack(snack_name,q,money)
        
        
        
            
        
        
        
