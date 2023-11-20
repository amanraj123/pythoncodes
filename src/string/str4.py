# reverse and capitalize first letter


str = "Hello"
output = ''
output1 = ''
i = len(str) - 1
while i >= 0:
    output = output + str[i]
    i = i - 1

print("\tUsing str.capitalize():---   ", output.capitalize())
i = len(str) - 1
output = output[0].upper() + output[1:]



print("\tusing split :---", output)
