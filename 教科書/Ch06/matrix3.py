# 定義matrixAdd() 方法用來進行矩陣相加
def matrixAdd(A, B):
    # 使用巢狀for迴圈將存放矩陣C的二維串列的每個元素初始化為0
    C = []
    for i in range(len(A)):
          C.append([])
          for j in range(len(A[i])):
              C[i].append(0)

    # 使用巢狀for迴圈將矩陣A、B相加，然後傳回結果，即矩陣C
    for i in range(len(A)):
        for j in range(len(A[i])):
            C[i][j] = A[i][j] + B[i][j]
    return C

# 定義printMatrix() 方法用來印出矩陣
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = '\t')
        print('\n')

# 將要相加的兩個矩陣指派給變數A、B
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# 呼叫matrixAdd() 方法將矩陣A、B相加，然後將結果指派給變數C
C = matrixAdd(A, B)

# 呼叫printMatrix()方法印出矩陣C
print("這兩個矩陣相加的結果如下：\n")
printMatrix(C)

