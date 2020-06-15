class Student:
    School = 'Greenway'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

s1 = Student(87,89,65)
s2 = Student(98,67,88)

print(s1.avg())
print(s2.avg())