import time


def countdown(num):
    print("Count down starting ...")
    while num > 0:
        yield num
        num = num - 1

values = countdown(5)
for x in values:
    print(x)
    time.sleep(1)

