class Student:
    School = 'Greenway'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.School

    @staticmethod
    def info():
        print("This is a student class..in abc module")

s1 = Student(87,93,65)
s2 = Student(78,56,97)

print(s1.avg())
print(Student.getSchool())

Student.info()