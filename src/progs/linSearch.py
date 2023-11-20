pos = -1
def linsearch(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False


def linsearchwhile(list,n):
    i = 0;
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


list = [5, 8, 4, 6, 9, 2]
n = 6
if linSearchWhile(list, n):
    print("found element at position", pos)
else:
    print("not found")


# using while loop

