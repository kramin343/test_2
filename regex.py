import re
name = input('Enter file name')
handle = open(name)
z = list()
sum = 0
for line in handle:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    print (y)
    for k in range(len(y)):
        i = int(y[k])
        z.append(i)
print ('final=',z)
for a in z:
    sum = sum + a
print(sum)