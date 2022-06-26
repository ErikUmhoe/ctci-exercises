class rotate_matrix:
    def print_matrix(self, matrix):
        for r in matrix:
            for c in r:
                print(c, end=" ")
            print()
        
    def rotate_90(self, matrix):
        size = len(matrix[0])
        self.print_matrix(matrix)
        new_matrix = [[0] * size] * size
        for colNum in range(0, size - 1):
            for rowNum in range(0, size - 1):
                new_matrix[colNum][size - rowNum - 1] = matrix[colNum][rowNum] 
        return new_matrix

myArr = [[11, 12, 5], [15, 6,10], [10, 8, 12]]
a = rotate_matrix()
a.print_matrix(a.rotate_90(myArr))