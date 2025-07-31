'''
Simplifies the construction of complex objects step bys tep without needing many constructors
Analogy:
Think of making a burger:
- bun,patty,cheese,sauce,lettuce
You dont want to pass 10 arguments to the constructor
'''
class Burger():
    def __init__(self,bun=None,patty=None,cheese=None,lettuce=None):
        self.bun = bun
        self.patty = patty
        self.cheese = cheese
        self.lettuce = lettuce
    
    def __str__(self):
        return f"Burger with {self.bun} and bla bla is made"
        
class BurgerBuilder():
    def __init__(self):
        self.bun = None
        self.patty = None
        self.cheese = None
        self.lettuce = None
    
    def add_bun(self,bun):
        self.bun=bun
        return self
    
    def add_patty(self,patty):
        self.patty = patty
        return self 
    
    def add_cheese(self,cheese):
        self.cheese = cheese
        return self 
     
    def add_lettuce(self,lettuce):
        self.lettuce = lettuce
        return self 
        
    def make_burger(self):
        return Burger(self.bun,self.patty,self.cheese,self.lettuce)
        
burger_builder = BurgerBuilder().add_bun("seseme").add_cheese("provolone").make_burger()
print(burger_builder)

'''
Note: Without returning self:

python# You'd have to call methods separately
builder = BurgerBuilder()
builder.add_bun("sesame")
builder.add_patty("beef")  
builder.add_cheese("cheddar")
builder.add_lettuce("iceberg")
burger = builder.make_burger()

With returning self:

python# You can chain methods together!
burger = BurgerBuilder().add_bun("sesame").add_patty("beef").add_cheese("cheddar").add_lettuce("iceberg").make_burger()

# Or formatted nicely:
burger = (BurgerBuilder()
          .add_bun("sesame")
          .add_patty("beef") 
          .add_cheese("cheddar")
          .add_lettuce("iceberg")
          .make_burger())
'''