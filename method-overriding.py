class A:

    def show(self):
        print("in A show")

class B(A):
     def show(self):
         super().show()
         print("in B show")


b1=B()
b1.show()
a1 = A()
a1.show()