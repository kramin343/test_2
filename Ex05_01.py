largest = None
smallest = None
while True:
    num1 = input("Enter a number: ")
    if num1 == 'done': 
        break
    try:
        num = float(num1)
    except:
        print('Invalid input')
        continue
    if largest == None:
        largest = num
        smallest = num
    if largest < num:
        largest = num
    if smallest > num:
        smallest = num
print("Maximum is",largest)
print("Minimum is",smallest)