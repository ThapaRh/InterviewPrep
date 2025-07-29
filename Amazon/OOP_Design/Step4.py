'''
Composition over inheritance
We use composition when we have to explain has a relation.
Composition is a design technique 
Dependency injection is a pattern built on that technique
'''

class Ink_Catridge():
    def __init__(self,color):
        self.color = color
    def get_color(self):
        return self.color

class Pen():
    def __init__(self,cartridge):
        self.cartridge = cartridge
    
    def write(self):
        print(f'Pen is writing using {self.cartridge.get_color()} color ink')
        
class Main:
    cartridge = Ink_Catridge("blue")
    pen = Pen(cartridge)
    pen.write()
    
    #without composition we would create an instance of Ink_Catridge() inside Pen class which would make these classes very coupled