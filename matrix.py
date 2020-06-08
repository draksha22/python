from numpy import *

m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('3 5 2; 7 2 1; 9 6 4')

print(diagonal(m1))

m3 = m1+m2
m4 = m1*m2

print(m3)
print(m4)
