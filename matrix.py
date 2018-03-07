class Matrix:
	def __init__(self, x1, x2, y1, y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2

	def add(self, givenMatrix):
		return Matrix(self.x1 + givenMatrix.x1, 
					  self.x2 + givenMatrix.x2,
					  self.y1 + givenMatrix.y1,
					  self.y2 + givenMatrix.y2)

	def muliply(self, givenMatrix):
		return Matrix(self.x2 * givenMatrix.x1 + self.x2 * givenMatrix.y1,
					  self.x1 * givenMatrix.x2 + self.x2 * givenMatrix.y2,
					  self.y1 * givenMatrix.x2 + self.x2 * givenMatrix.y1,
					  self.y1 * givenMatrix.x2 + self.y1 * givenMatrix.y2)

	def print(self):
		print("[" + str(self.x1) + ", " + str(self.x2) + ", " + str(self.y1) + ", " + str(self.y1) + "]")