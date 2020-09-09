name = input("What is your name? ")
cookies = int(input("How many cookies would you like? "))

print("Hi %s! " % (name))

if 1 <= cookies < 10 :
	print("Are you sure it's enough?")
elif 10 <= cookies < 20 :
	print("I agree cookies are delicious!")
elif 20 <= cookies < 51 :
	print("Be careful, it's getting too much")
elif cookies > 50 :
	print("No way, it's getting too much")
	cookies = 50
else:
	print("Something must be wrong, I give you 10 cookies")
	cookies = 10

output = "Here are your cookies: "
for cookie in range(cookies):
	output += "cookie "

print(output)