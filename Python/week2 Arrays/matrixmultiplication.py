# Classical Algorithm and Problem on 2D-Arrays
# Matrix multiplication is a classical matrix problem where each element of the resulting matrix is calculated as the dot product of a row from the first matrix and a column from the second. It combines two matrices to form a new one based on this rule.

# Core Idea: For C[i][j], sum the product of corresponding elements from row i of matrix A and column j of matrix B: C[i][j] = A[i][0]*B[0][j] + A[i][1] * B[1][j] + ... + A[i][k] * B[k][j]






def multiply(arr, brr):
    n = len(arr)

    # to store the resultant matrix
    res = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += arr[i][k] * brr[k][j]

    return res


if __name__ == "__main__":
    arr = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

    brr = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

    result = multiply(arr, brr)

    for row in result:
        print(row)