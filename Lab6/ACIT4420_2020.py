"""
Marit Øye Gjersdal
s348588
"""

from Course_graded import Course_grade

class ACIT4420_2020(Course_grade):

	def __init__(self):
		super().__init__()
		self._assignment_weights = [5, 7, 10, 6, 7, 8, 7]	# 7 graded assignments
		self._exam_weight = 50	# 50% final exam