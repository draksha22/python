class Computer:

    def __init__(self):
        self.name  = 'Rachel'
        self.age = 28

    def update(self):
        self.age = 30

c1 = Computer()
c2 = Computer()

c1.name = 'Emma'
c1.age = 12

c1.update()

print(c1.name)
print(c1.age)