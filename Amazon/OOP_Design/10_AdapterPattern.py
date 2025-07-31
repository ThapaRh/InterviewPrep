'''
Less incompatible interfaces work together - like translator between two system
Analogy:
A phone charger adapter lets USB-C phone plug into a wall outlet
'''
#you have an oldprinter that expects input via old_print() but your new system uses print_document()

class OldPrinter():
    def old_print(self,text):
        print(f'old printer: {text}')
    
class PrintDocument():
    def print_document(self,text):
        pass

class PrintAdapter(PrintDocument):
    def __init__(self,old_printer):
        self.old_printer = old_printer
    
    def print_document(self,text):
        return self.old_printer.old_print(text)
    
    
adapter = PrintAdapter(OldPrinter())
adapter.print_document("this is new text")

#we use this in legacy systems and apis or while integrating third party tools