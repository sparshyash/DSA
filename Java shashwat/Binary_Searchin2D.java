import java.util.Arrays;


public class Binary_Searchin2D {
    public static void main(String[] args) {
        // We can do by for loop O(n^2)
        // arr[i][j]==target return new int[]{i,j}


        // Case -1 if rows are sorted and columns are sorted [[1,2,3],[4,5,6]]

        int[][] arr = {{1, 2, 3}, {4, 5, 6}};
        int target = 5;
        
        System.out.println(Arrays.toString(search(arr, target)));
    }

    public static int[] search(int[][] arr, int target) {
        int row = 0;
        int col = arr[0].length - 1;

        while (row < arr.length && col >= 0) {
            if (arr[row][col] == target) {
                return new int[]{row, col};
            } else if (arr[row][col] > target) {
                col--;
            } else {
                row++;
            }
        }
        return new int[]{-1, -1};

    }
}