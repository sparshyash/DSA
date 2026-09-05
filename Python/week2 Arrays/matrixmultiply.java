

public class matrixmultiply {
    static int[][] multiply(int[][] arr, int[][] brr){
    
        int n = arr.length;
    
        // to store the resultant matrix
        int[][] res = new int[n][n];
    
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    res[i][j] += arr[i][k] * brr[k][j];
                }
            }
        }
    
        return res;
    }

    public static void main(String[] args) {
        int[][] arr = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
        int[][] brr = { { 9, 8, 7 }, { 6, 5, 4 }, { 3, 2, 1 } };

        int ans[][] = new int[arr.length][brr.length];
        ans= multiply(arr, brr);
        for (int i = 0; i < ans.length; i++) {
            for (int j = 0; j < ans.length; j++) {
                System.out.print(ans[i][j] + " ");
            }
            System.out.println();
        }
    }
}
