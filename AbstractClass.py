from abc import ABC,abstractmethod

class Computer():
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("its running")

class Whiteboard(Computer):
    def write(self):
        print("its writing")

class Programmer:
    def work(self,com):
        print("solving bugs")
        com.process()

com1 = Laptop()
com2 = Whiteboard()
prog1 = Programmer()
prog1.work(com2)