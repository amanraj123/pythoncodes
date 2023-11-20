s= input("Enter some string to reverse: ")
output = ''
i = len(s) - 1
while i >= 0:
    output = output + s[i]
    i = i-1
print(output)

