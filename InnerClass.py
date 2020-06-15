class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = 'Dell'
            self.cpu = 'i5'
            self.ram = 16

s1 = Student('rachel', 1)
s2 = Student('rhea', 2)

s16.show()

lap1 = s1.Laptop()
lap2 = s2.Laptop()

print(id(lap1))
print(id(lap2))