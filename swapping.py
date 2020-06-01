a,b = 5,6

temp = a
a = b
b = temp
print(a,b)

a = a + b
b = a - b
a = a - b
print(a,b)

a,b = b,a
print(a,b)

a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)