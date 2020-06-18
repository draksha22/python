def topten():
      yield 1
      yield 2
      yield 3
      yield 4

values = topten()

print(values.__next__())

for i in values:
      print(i)