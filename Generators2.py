def TopTen():

    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1

values = TopTen()

# printing values using iterator

print(next(values))
print(next(values))
print(next(values))

# printing values using for loop

for i in values:
    print(i)