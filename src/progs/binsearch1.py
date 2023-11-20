
# binary search list mist be sorted


pos = -1

def binsearch(list, n):
    l = 0
    u = len(list) - 1
    while l <= u :
        mid = (l + u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n :
                l = mid + 1
            else:
                u = mid -1
    return False


list = [4,11,33,44,66,99,888,999,2,3,4,5]

print("\noriginal list before sorting", list)
list.sort()
print("new list after sort", list)
n = 999

if binsearch(list,n):
    print("\nFound at pos ",  pos)
else:
    print("\nnot found")
