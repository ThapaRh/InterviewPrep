'''
This is basically using the interface to define the contract and creating other classes that uses that contract 
and then creating strategy class which will choose specific class to use as a DI

Strategy is behavioral pattern unlike factory which is creational pattern
factory is used to create objects but strategy is used to select and switch behavior
'''

class TextFormatter:
    def format(self,text):
        pass #this will act like interface in python

class UpperCaseFormatter(TextFormatter):
    def format(self,text):
        return text.upper()
    
class LowerCaseFormatter(TextFormatter):
    def format(self,text):
        return text.lower()
    
class TextEditorStrategy():
    def __init__(self,formatter:TextFormatter):
        self.formatter = formatter
    
    def publish(self,text):
        formatted_text = self.formatter.format(text)
        print(formatted_text)

class Main:
    editor = TextEditorStrategy(UpperCaseFormatter())
    editor.publish("Hello World.")