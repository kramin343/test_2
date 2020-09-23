hrs = input("Enter Hours:")
try:
	h = float(hrs)
except:
	h = 45
rate = 10.50
pay = 0
if h > 40:
	pay = ((h-40)*1.5*rate)+(40*rate)
else:
	pay = h*rate
print(pay)