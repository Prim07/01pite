from matrix import Matrix

matrix_1 = Matrix(4, 5, 6, 7)
matrix_2 = Matrix(2, 2, 2, 1)

matrix_3 = matrix_2.add(matrix_1)
matrix_4 = matrix_2.multiply(matrix_1)

matrix_3.print()
matrix_4.print()