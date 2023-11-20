try:
    x = int( input("Enter first number: "))
    y = int( input("Enter second number: "))
    print("The result: ", int(x/y))
except BaseException as msg:
    print("type of exception is : ", type(msg))
    print("type of exception is : ", msg.__class__)
    print("type of exception class is : ", msg.__class__.__name__)

'''
#ZeroDivisionError
#ValueError: invalid literal for int() with base 10: 'tes'

print("The result: ", int(x/y))


print('statement-1')
print(1/0)
print('statement 3')
'''