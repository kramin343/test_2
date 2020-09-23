fname = input("Enter file name: ")
fh = open(fname)
tot = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
		continue
    a = line.find('0')
    b = float(line[a:])
    tot = tot + b
    count = count + 1
x = tot/count
print("Average spam confidence:",x)