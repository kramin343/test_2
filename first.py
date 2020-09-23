largest = None
smallest = None
while True:
    num1 = input("Enter a number: ")
    try:
        num = float(num1)
    except:
        print('Invalid input')
        continue
    if num == "done" : 
        break
    if largest == none:
        largest = num
        smallest = num
    if largest < num:
        largest = num
    if smallest > num:
        smallest = num
print("Maximum is",largest)
print("Minimum is",smallest)