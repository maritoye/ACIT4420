"""
Marit Øye Gjersdal
s348588
"""

from Course_graded import Course_grade

class ACIT4420_2019(Course_grade):

	def __init__(self):
		super().__init__()
		self._assignment_weights = [0,0,0,0,0,0,0]	# no graded assignments
		self._exam_weight = 100	# 100% final exam