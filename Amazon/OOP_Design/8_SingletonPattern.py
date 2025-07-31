'''
The singleton pattern ensures that the class only has one instance, and provides a global point of access to it
real life analogy:
A system should have only one logger, one configurationManager and one DatabaseConnection
'''

class Logger():
    _instance = None #class level variable
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger,cls).__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self,message):
        self.logs.append(message)
    
    def show_logs(self):
        for msg in self.logs:
            print(msg)

class Main:
    logger0 = Logger()
    logger1 = Logger()
    logger0.log("Log 0 is logged")
    logger1.show_logs()
    
    
#one more singleton class creation for practice
class Singleton():
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton,cls).__new__(cls)
            cls._instance.logs = []
        return cls._instance