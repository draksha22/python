class Cars:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = 'BMW'


c1 = Cars()
c2 = Cars()

c1.mil = 8

Cars.wheels = 5

print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)