try:
    print(1/0)
except ZeroDivisionError as msg:
    print("type of exception is : ", type(msg))
    print("type of exception is : ", msg.__class__)
    print("type of exception class is : ", msg.__class__.__name__)



