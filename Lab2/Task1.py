intro = """
s - Store program
l - List daily program
x - Exit
"""
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
modes = ["s", "l", "x"]
program = []

for i in range(len(days)):
	list = []
	for j in range(25):
		list.append(" ")
	list[0] = days[i]
	program.append(list)

while True:
	print(intro)
	mode = input(str("Choose from the list: "))

	while mode not in modes:
		mode = input(str("Please enter a valid input: "))

	if mode == "x":
		exit()

	if mode == "s":
		day = str(input("Which day? "))
		time = int(input("What time? "))
		event = input(str("What is the program? "))
		
		program[days.index(day)].insert(time+1, event)
		print("Program has been stored")

	if mode == "l":
		day = str(input("Which day? "))
		hour = 0
		for i in range(1 ,25):
			print(str(hour) + ":00 " + program[days.index(day)][i])
			hour+=1