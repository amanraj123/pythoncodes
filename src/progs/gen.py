def square(n):
    for i in range(n):
        #return i**2
        yield i**2


a = square(3)
print(next(a))
print(next(a))

print(next(a))
print(next(a))