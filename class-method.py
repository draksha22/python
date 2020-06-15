class Student:
    School = 'Greenway'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod

    def info(cls):
        return cls.School

s1 = Student(54,98,67)
s2 = Student(98,76,87)

print(s1.avg())
print(s1.info())
print(s2.avg())
print(s2.info())