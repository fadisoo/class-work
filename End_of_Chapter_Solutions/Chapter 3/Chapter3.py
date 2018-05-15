#Chapter 3 Exercies 
#3.1

hours = float(input('Hours Wroked: '))
rate = float(input('Enter Rate: '))
if hours > 40:
	pay = hours * rate + (hours - 40) * hours * rate * 1.5
else:
	pay = rate * hours
print("")
print('Pay: $', pay)

#3.2

try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print("")
    print("Both entries must be numbers")
    quit()
if hours > 40:
    pay = hours * rate + (hours - 40) * rate * 0.5
else:
    pay = hours * rate
print("")
print("Pay $",pay)

# 3.3

try:
    score = float(input('Enter 0.0 to 1.0: '))
    if score >= 0.0 and score <= 1.0:
        pass
    else:
        quit()
except:
    print("Bad Score!!") 
    quit()
if score >= 0.9:
    print("A") 
elif score >= 0.8:
    print("B") 
elif score >= 0.7:
    print("C") 
elif score >= 0.6:
    print("D") 
else:
    print("F") 	
quit()