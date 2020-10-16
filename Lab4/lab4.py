"""
Marit Øye Gjersdal
s348588
"""

from reportlab.pdfgen import canvas
from operator import itemgetter
import psutil


def main():
	process_list = processes()
	create_pdf(process_list)


def processes():
	"""
	creates a list of dictionary sets containing all names and process ids of running processes
	:return: list of dictionaries
	"""
	process_list = []
	for p in psutil.process_iter():
		process_dict = p.as_dict(attrs=['name', 'pid'])
		process_list.append(process_dict)

	return process_list


def create_pdf(process_list):
	"""
	sorts all the processes alphabetically by name, and writes a pdf containing one page of process names and ids
	:param process_list: list of dictionaries
	:param output: name of the process to be created
	"""
	c = canvas.Canvas("processes.pdf")
	sorted_list = sorted(process_list, key=itemgetter('name'))
	c.drawString(100, 780, "Currently running processes:")
	pos = 750
	for line in sorted_list:
		if pos > 50:
			c.drawString(100, pos, line["name"] + "  " + str(line["pid"]))
			pos -= 15
		else:
			break

	c.showPage()
	c.save()


if __name__ == '__main__':
	main()