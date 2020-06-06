from array import *
arr = array('i',[1,2,3,4,5])
print(arr[::-1])



from array import *
arr = array('i',[1,2,3,4,5])
k = len(arr)-1
while k > -1:
    print(arr[k])
    k-=1


from array import *
a = array('i',[1,2,3,4,5,])
b = array('i',[])
for i in range(1,6):
    b.append(a[-i])
    print(b)
