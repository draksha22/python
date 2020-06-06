from array import *
vals = array('i', [3,55,23,7,52,12,66,45,4,31])
vals=sorted(vals)
print(vals)



from array import *
a = array('i',[22,65,33,5,10])
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            a[i],a[j] = a[j],a[i]
        print(a)

