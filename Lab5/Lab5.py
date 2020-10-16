"""
Marit Øye Gjersdal
s348588
"""

import re

f = open("canvas.txt", encoding="utf-8")
data = f.read()

def main():
	email_oslomet()
	email_all()
	activity_time()
	sys_id()
	activity_total()
	student_names()
	activity_ten()
	august()
	

def email_oslomet():
	"""
	Find all standard oslomet student email addresses
	 "s" + 6-7 digits + "@oslomet.no"
	"""
	print("\nFind all standard oslomet student email addresses:")
	print(re.findall("[s]\d{5,6}@oslomet\.no", data))


def email_all():
	"""
	Find all email addresses
	username (chars or numbers) + "@" (+ subdomain) + "." + domain + "." + tld
	"""
	print("\nFind all email addresses:")
	print(re.findall("(?:\w+\.*\w){1,}@(?:\w+\.){1,2}\w+", data))


def activity_time():
	"""
	Find the last activity time of all students
	date (1-2 digits) + month (3 chars) + "at" + hours (0-23, 1 or 2 digits) + minutes (00-59, 2 digits)
	"""
	print("\nFind the last activity time of all students (same output as required, including teachers):")
	print(re.findall("\d{1,2}[ ]\w[a-zA-Z]{2}[ ]at[ ]\d{1,2}:\d{2}", data))

	print("\nFind the last activity time of all students (STUDENTS ONLY):")
	print(re.findall("Student\n(\d{1,2}[ ]\w[a-zA-Z]{2}[ ]at[ ]\d{1,2}:\d{2})", data))


def sys_id():
	"""
	Find the system ids of the students
	"fs:" + 3 digits + ":" 5-7 digits  (task sheet says 6-7, but one student only have 5)
	"""
	print("\nFind the system ids of the students (same output as required, including teachers):")
	print(re.findall("fs:\d{3}:\d{5,7}", data))

	print("\nFind the system ids of the students (STUDENTS ONLY):")
	print(re.findall("(fs:\d{3}:\d{5,7})(?:\t*\n.*){0,3}Student", data))


def activity_total():
	"""
	Find the total activity time of the users on Canvas
	hours (2 digits) + ":" + minutes (2 digits) + ":" + seconds (2 digits)
	or minutes (2 digits) + ":" + seconds (2 digits)
	do not match the last activity time: I chose to  do this by checking if the string is in its own separate line
	"""
	print("\nFind the total activity time of the users on Canvas:")
	print(re.findall("\n((?:\d{2}:){1,2}\d{2})\n", data))


def student_names():
	"""
	Find the names of the students
	# The output in the assignment sheet does not include norwegian special characters, however I wanted them to be included
	# The \n at beginning and end is there to assure only the names on separate lines are included (so all names won't be included twice)
	# First and middle names (1 to 4 names, each consisting of at least one letter, and a space after the name
	# Last name (consisting of at least one letter)
	"""
	print("\nFind the names of the students (same output as required, including teachers):")
	print(re.findall("\n((?:[a-zA-ZæøåÆØÅé-]+ ){1,4}[a-zA-ZæøåÆØÅé-]+)\n", data))

	print("\nFind the names of the students (STUDENTS ONLY):")
	print(re.findall("\n((?:[a-zA-ZæøåÆØÅé-]+ ){1,4}[a-zA-ZæøåÆØÅé-]+)(?:\n.*){0,5}Student", data))


	"""
	first wanted to use this as it requires capital first letter in first and last names,
	however one users last name doesnt have capital letter, 
	and since the task sheet output includes that name I chose to remove this requirement:
	
	print(re.findall("[\n]((?:[A-ZÆØÅ][a-zA-ZæøåÆØÅé-]+ ){1,4}[A-ZÆØÅ][a-zA-ZæøåÆØÅé-]+)[\n]", data))
	"""


def activity_ten():
	"""
	Find all users with name where the user activity was more than 10 hours
	get the name (same way as previous), skip any characters or numbers for up to five lines,
	followed by any number from 10-99 + : 2 digits : 2 digits + line break
	"""
	print("\nFind all users with name where the user activity was more than 10 hours:")

	print(re.findall("\n((?:[a-zA-ZæøåÆØÅé-]+ ){1,4}[a-zA-ZæøåÆØÅé-]+)(?:\n.*){0,5}[1-9]\d:\d{2}:\d{2}", data))


def august():
	"""
	Find all users with name where the last user login was in August
	get the name (same way as previous), skip any characters or numbers for up to four lines, followed by one or two digits then "Aug"
	"""
	print("\nFind all users with name where the last user login was in August:")

	print(re.findall("\n((?:[a-zA-ZæøåÆØÅé-]+ ){1,4}[a-zA-ZæøåÆØÅé-]+)(?:\n.*){0,4}\d{1,2} Aug", data))


if __name__ == '__main__':
	main()