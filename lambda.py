f = lambda a,b : a+b
result = f(5,6)
print(result)

from functools import *
nums = [3,2,6,8,4,6,2,9]
evens = list(filter(lambda a : a%2 == 0,nums))
print(evens)
doubles = list(map(lambda a : a*2,evens))
print(doubles)
sum = reduce(lambda a,b : a+b,doubles)
print(sum)