class Hello:
    def run(self):
        for i in range(5):
            print("Hello",i)


class Hi:
    def run(self):
        for i in range(5):
            print("Hi",i)

t1 = Hello()
t2 = Hi()

t1.run()
t2.run()