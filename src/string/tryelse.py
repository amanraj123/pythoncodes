try:
    print("try")
    print(1/0)
except:
    print("except")
else:
    print("else")
finally:
    print("finally")

print("#"*30)

f=None
try:
    f=open('abc1.txt', 'r')
except:
    print("can not open file")
else:
    print("file opened succseesfully")
    print("the content is ")
    print ("#"*30)
    print(f.read())
finally:
    if f is not None:
        f.close()
