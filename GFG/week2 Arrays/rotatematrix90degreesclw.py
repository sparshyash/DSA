
# Rotate Square Matrix by 90 Degrees is a classical problem based on matrices, where a square 2D matrix is rotated 90 degrees clockwise. In this transformation, the first row becomes the last column, the second row becomes the second-last column, and so on.








def rotateMatrix(mat):
    n=len(mat)

    #  Consider all cycles one by one
    for   i in range(n//2):
        
        
        # Consider elements in group of 4
        #  as P1, P2, P3 & P4 in current square
        for j in range(i,n-i-1):

    
            mat[i][j]  ,mat[j][n - 1 - i] ,mat[n - 1 - i][n - 1 - j] , mat[n - 1 - j][i]= mat[j][n - 1 - i], mat[n - 1 - i][n - 1 - j] ,  mat[n - 1 - j][i] , mat[i][j]
            
            
        
if __name__=="__main__":
    arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    rotateMatrix(arr)
    print(arr)