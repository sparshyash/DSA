def transpose(mat):
    rows = len(mat)
    cols = len(mat[0])

    #  Create a result matrix of size
    #  cols x rows for the transpose
    tMat =  [[0 for _ in range(rows)]for _ in range(cols)]

    # Fill the transposed matrix by
    # swapping rows with columns
    for i in range(rows) :
        for j in range(cols) :
            # Assign transposed value
            tMat[j][i] = mat[i][j];
        
    

    return tMat

if __name__=="__main__":
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    ans =transpose(arr)
    print(ans)