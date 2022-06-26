class zero_matrix:
    def print_matrix(self, matrix):
        for r in matrix:
            for c in r:
                print(c, end=" ")
            print()
        
    
    def matrix_zero(self, matrix):
        cols = len(matrix[0])
        rows = len(matrix)
        print(f"Rows: {rows}, Cols:{cols}")
        zeroes = []
        for row in range(0, rows):
            for col in range(0, cols):
                if matrix[row][col] == 0:
                    zeroes.append((row, col))
        for i in range(0, len(zeroes)):
            row = zeroes[i][0]
            col = zeroes[i][1]
            matrix[row] = [0] * cols
            for j in range(0, rows):
                matrix[j][col] = 0
        return matrix

matrix = [[0, 1, 2, 4], [7,8,9,0], [3,1,5,7]]
a = zero_matrix()
a.print_matrix(matrix)
print("-------------------------------------")
a.print_matrix(a.matrix_zero(matrix))