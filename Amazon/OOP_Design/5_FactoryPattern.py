'''
Used to create objects without exposing the exact class being instantiated.
So real world example is : going to store and asking give me gel pen(we dont care how it's made, we just get the pen from store)
'''
class Pen(): #creating pen interface in python
    def write(self):
        pass

class BallPen():
    def write(self):
        print("Writing using ball pen")

class FountainPen():
    def write(self):
        print("Writing using fountain pen")
        
class NoBallPen():
    def write(self):
        print("Writing using no ball pen")
        
class GelPen():
    def write(self):
        print("Writing using gel pen")
        

class Factory():
    @staticmethod
    def create_pen(pen_type):
        if pen_type == "gel":
            return GelPen()
        elif pen_type == "ball":
            return BallPen()
        elif pen_type == "no ball":
            return NoBallPen()
        elif pen_type == "fountain":
            return FountainPen()

class Main:
    pen = Factory.create_pen("gel")
    pen.write()
    