name = input("What is your name? ")
cookies = int(input("How many cookies would you like? "))

output = "Hi %s, here are your cookies: " % (name)
for cookie in range(cookies):
	output += "cookie "

print(output)