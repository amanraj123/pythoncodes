s= "hello world"
# output -- > olleh dlrow

l = s.split()
l1 = []

for word in l:
    l1.append(word[::-1])
output = ' '.join(l1)

print(l1)
print(output)
print(output[::-1])