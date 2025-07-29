'''
OOP is daunting, I just had a mini crash yesterday and today because I wasnot sure where to begin and where to end
And alas i just realized i can make my chat gpt walk me through the oop concepts and practice step by step, ask as many dumb questions(no question is dumb btw) and have my own best friend/mentor on my hand(When AI takes over,it'll not kill me first cause I am saying good things about AI lolol)
So my chatu is giving me step by step approach to solving the or cracking OOP interview
'''
#Step 1: Creating classes and objects
#think in terms of what an entity is and what can it do
#lets think about a pen, the attributes can be ink, brand and cost and the actions can be write and refill

class Pen:
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand
    
    def write(self):
        print("pen is writing")
        
    def refill(self):
        print("lets refill")
        
#this wasnot that bad was it?