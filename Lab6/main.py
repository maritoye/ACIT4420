"""
Marit Øye Gjersdal
s348588
"""

from ACIT4420_2019 import ACIT4420_2019
from ACIT4420_2020 import ACIT4420_2020

def main():
	a = ACIT4420_2020()
	a.set_graded_assignments([70, 70, 70, 70, 70, 70, 70])
	a.set_graded_assignment(2, 100)
	a.set_exam(76)
	print(a.get_grade())

	a2 = ACIT4420_2019()
	a2.set_assignments([True, True, True, True, True, True, True])
	a2.set_exam(76)
	print(a2.get_grade())

	b = ACIT4420_2020()
	b.set_graded_assignments([20, 20, 20, 20, 20, 20, 20])
	b.set_graded_assignment(2, 100)
	b.set_exam(84)
	print(b.get_grade())

	b2 = ACIT4420_2019()
	b2.set_assignments([True, True, True, True, True, True, True])
	b2.set_exam(84)
	print(b2.get_grade())


if __name__ == '__main__':
	main()