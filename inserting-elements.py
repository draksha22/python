from array import *
arr = array('i',[])
x = int(input("enter the length of array"))
for i in range(x):
    n = int(input("enter the value you want to insert"))
    arr.append(n)
    print(arr)