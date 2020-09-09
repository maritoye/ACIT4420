amount = int(input("How many numbers do you have? "))
total = 0

for number in range(amount):
	total += int(input(str("What is the %s. number? ") % (number+1)))

print("The average is: " + str("{:.2f}".format(total / amount)))