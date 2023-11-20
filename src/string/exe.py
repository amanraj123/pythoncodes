import os
try:
    x = int( input("Enter first number: "))
    y = int( input("Enter second number: "))
    os._exit(1)
    print("The result: ", int(x/y))
    os._exit(0)
except ZeroDivisionError as msg:
    print("type of exception is : ", type(msg))
    print("type of exception is : ", msg.__class__)
    print("type of exception class is : ", msg.__class__.__name__)
except:
    print("Default except block, please provide valid inputs")
finally:
    print("finally block")


'''
#ZeroDivisionError
#ValueError: invalid literal for int() with base 10: 'tes'

print("The result: ", int(x/y))


print('statement-1')
print(1/0)
print('statement 3')
'''