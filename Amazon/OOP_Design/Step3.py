'''
Inheritance:
This is so basic, all of us should know this. I am not even explaining
'''
class Animal:  
    def __init__(self,name="Bob"):
        self.name = name
    
    def get_name(self):
        print(f'Hello. My name is {self.name}')
        
    def sleep(self):
        print("Animal is sleeping.")

class Dog(Animal):
    def bark(self):
        print(f'{self.name} barks.')
    
    def sleep(self):
        print("Dog is sleeping.")

class Cat():
    def sleep(self):
        print("Cat is sleeping.")

class Main:
    #this is example of inheritance
    dog = Dog("Rob")
    dog.get_name() 
    dog.bark()
    
    #this is polymorphism
    def test_sleep(animal:Animal):
        animal.sleep()
    
    arr = [Animal(),Dog(),Cat()]
    for a in arr:
        test_sleep(a)