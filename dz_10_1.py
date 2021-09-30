class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, matrix_other):
        sum_ = []
        for idx in range(len(self.matrix)):
            m = []
            for id_ in range(len(self.matrix[idx])):
                element = self.matrix[idx][id_] + matrix_other.matrix[idx][id_]
                m.append(element)
            sum_.append(m)
        return Matrix(sum_)

    def __str__(self):
        return f"{self.matrix}"


mat_1 = [[1, 2, 3, 8], [4, 5, 6, 9]]
mat_2 = [[13, 14, 15, 11], [11, 1, 77, 7]]
ob_1 = Matrix(mat_1)
ob_2 = Matrix(mat_2)
result = ob_1 + ob_2
print(result)
print(type(result))
