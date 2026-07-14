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