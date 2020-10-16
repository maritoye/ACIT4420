"""
Marit Øye Gjersdal
s348588
"""

intro = "s - Store program \nl - List daily program \nx - Exit"
days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
modes = ["s", "l", "x"]

program = [[" "] * 24 for i in range(len(days))]

print(intro)

while True:
	mode = input(str("Choose from the list: "))

	while mode not in modes:
		mode = input(str("Please enter a valid input: "))

	if mode == "x":
		exit()

	if mode == "s":
		day = str(input("Which day? "))
		time = int(input("What time? "))
		event = input(str("What is the program? "))
		
		program[days.index(day)].insert(time, event)
		print("Program has been stored")

	if mode == "l":
		day = str(input("Which day? "))
		hour = 0
		for i in range(0 ,24):
			print(str(hour) + ":00 " + program[days.index(day)][i])
			hour+=1