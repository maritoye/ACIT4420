"""
Marit Øye Gjersdal
s348588
"""

class Course_grade():
	def __init__(self):
		self._assignment_weights = []
		self._exam_weight = 0
		self._graded_exam = 0
		self._assignments = []
		self._graded_assignments = []


	def set_assignment(self, assignment, grade):
		# input is true or false
		self._assignments[assignment] = grade


	def set_assignments(self, assignments):
		# input is a list of true or false
		self._assignments = assignments


	def set_graded_assignment(self, assignment, grade):
		# input is percentage
		self._graded_assignments[assignment] = grade


	def set_graded_assignments(self, assignments):
		# input is a list of percentages
		self._graded_assignments = assignments


	def set_exam(self, grade):
		# input is a percentage
		self._graded_exam = grade

	def calculate_final_grade(self, grade):
		if grade < 40:
			return "F"
		elif 40 <= grade < 50:
			return "E"

		elif 50 <= grade < 60:
			return "D"

		elif 60 <= grade < 80:
			return "C"

		elif 80 <= grade < 90:
			return "B"

		elif 90 <= grade < 100:
			return "A"

	def get_grade(self):
		"""
		Assumptions made: task sheet says all assignments must be delivered, but that does not mean they all have to be
		passed. Therefore not handed in assignment is represented as -1 (both for graded and non-graded assignments).
		This way a student can fail an assignment they handed in without failing the whole class
		"""

		graded_assignments_grade = 0
		assignments_grade = 0

		# if exam percentage is less than 40, final grade is F
		if self._graded_exam < 40:
			return "F"


		# handle graded assignments, if the _graded_assignments list is not empty
		if self._graded_assignments:
			# for each assignment add the percentage given the weight of that assignment
			for assignment in range(len(self._graded_assignments)):
				# if one assignment is not delivered, give grade F
				if assignment == -1:
					return "F"

				graded_assignments_grade += self._assignment_weights[assignment]/100 * self._graded_assignments[assignment]

			# grade F if total score of assignments is less than 40 percent
			if (graded_assignments_grade * 2) < 40:
				return "F"


		# handle graded assignments, if the _assignments list is not empty
		elif self._assignments:
			passed_assignments = 0

			# must submit ALL assignments, if not grade is F
			for assignment in self._assignments:
				# not delivered assignments are represented as -1 (since not delivered and not passed are two separate things)
				if assignment == -1:
					return "F"

				if assignment:
					passed_assignments +=1

			# optional: grade F if less than 40 percent of assignments are passed
			#if (passed_assignments/len(self._assignments))*100 < 40:
				#return "F"

		#calculate exam grade points given weight of exam
		exam_grade = self._exam_weight/100 * self._graded_exam

		# add up total points, and call the calculate function to get the final grade
		return self.calculate_final_grade(graded_assignments_grade + assignments_grade + exam_grade)

