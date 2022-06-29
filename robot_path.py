# from re import M
# import pprint as pp


# def path_exists(matrix):
#     numRows = len(matrix) - 1
#     numCols = len(matrix[0]) - 1
#     if numRows == 0 and numCols == 0:
#         return True
#     row = 0
#     col = 0
#     m2 = [[0 ]* len(matrix[0])] * len(matrix)
#     return _path_exists(matrix, m2,row + 1, col, numRows, numCols) or _path_exists(matrix,m2, row, col + 1, numRows, numCols)

# def _path_exists(matrix, m2, row, col, rows, cols):
#     print(f"R: {row}, C: {col}")
#     if matrix[row][col] == -1:
#         return False
#     if row == rows and col == cols:
#         m2[row][col] = 'x'
#         for n in m2:
#             print(n)
#         return True
#     if row == rows:
#         return _path_exists(matrix,m2, row, col + 1, rows, cols)
#     if cols == col:
#         return _path_exists(matrix,m2, row + 1, col, rows, cols)
#     m2[row][col] = 'x'
#     return _path_exists(matrix,m2, row + 1, col, rows, cols) or _path_exists(matrix,m2, row, col + 1, rows, cols)

# def get_path(matrix):
#     numRows = len(matrix)
#     numCols = len(matrix[0])
#     if numRows == 0 and numCols == 0:
#         return None
#     path = [[0] * numCols] * numRows
#     for x in path:
#         print(x)
#     print("-----------------------")
#     return _get_path(matrix, path, 0, 0, numRows, numCols)

# def _get_path(matrix, path, row, col, rows, cols):
#     try:
#         if row >= rows or col >= cols or matrix[row][col] == -1:
#             return

#         if row < rows:
#             _get_path(matrix, path, row + 1, col, rows, cols)            
#         if col < cols:
#             _get_path(matrix, path, row, col + 1, rows, cols)
#         path[row][col] = 'x'
#         return path
#     except:
#         print(f"Row: {row}")
#         print(f"Col: {col}")
#         print(f"Path:\n{path}")



# matrix = [
#         [0, 0, 0], 
#         [-1, 0, 0],
#         [-1, 0 , 0],
#         [-1, 0, 0]]

# # print(path_exists(matrix))
# pp.pprint(get_path(matrix))

#Solution with recursion O(2^r+c)
def getPath(maze):
    if maze == None or len(maze) == 0:
        return None
    path = [] 
    if isPath(maze, len(maze)-1, len(maze[0])-1, path):
        return path
    return None

def isPath(maze, row, col, path):
    #if out of bounds or not available, return
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    
    isAtOrigin = (row == 0) and (col == 0)

    #if there's a path from the start to here, add my location
    if isAtOrigin or isPath(maze, row, col-1, path) or isPath(maze, row-1, col,path):
        point = (row,col)
        path.append(point)
        return True

    return False

#Solution with memoization 
def getPathMemoized(maze):
    if maze == None or len(maze) == 0:
        return None
    path = []
    failedPoints = []
    if isPathMemoized(maze, len(maze)-1, len(maze[0])-1, path, failedPoints):
        return path
    return None

def isPathMemoized(maze, row, col, path, failedPoints):
    #If out of bounds or not availabe, return
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    
    point = (row,col)

    # if we've already visisted this cell, return
    if point in failedPoints:
        return False

    isAtOrigin = (row == 0) and (col == 0)

    #If there's a path from start to my current location, add my location
    if isAtOrigin or isPathMemoized(maze, row, col-1, path, failedPoints) or isPathMemoized(maze, row-1, col, path, failedPoints):
        path.append(point)
        return True

    failedPoints.append(point) 
    return False


print(getPath([[True, True],[True,True]]))    
print(getPathMemoized([[True,True], [False,True]]))