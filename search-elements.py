from array import *
arr = array('i',[])
x = int(input("Enter length of an array"))
for i in range(x):
    n = int(input("Enter the element you want to insert"))
    arr.append(n)
    print(arr)

val = int(input("Enter the value for search"))
k=0
for i in arr:
    if i==val:
        print(k)
    k+=1

from array import *
arr = array('i',[])
x = int(input("Enter length of an array"))
for i in range(x):
    n = int(input("Enter the element you want to insert"))
    arr.append(n)
    print(arr)

val = int(input("Enter the value for search"))
print(arr.index(val))
