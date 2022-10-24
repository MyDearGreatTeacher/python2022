matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# 定義printMatrix() 方法用來印出矩陣
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = '\t')
        print('\n')

# 呼叫printMatrix() 方法印出矩陣
printMatrix(matrix)
