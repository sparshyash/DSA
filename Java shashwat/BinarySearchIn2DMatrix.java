package Kunal;
import java.util.Arrays;

public class BinarySearchIn2DMatrix {
    public static void main(String[] args) {
        int[][] arr = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
            {10, 11, 12}
        };
        System.out.println(Arrays.toString(search(arr, 5)));
    }

    static int[] binarySearch(int[][] matrix, int row, int colStart, int colEnd, int target) {
        while (colStart <=colEnd) {
            int mid = colStart + (colEnd - colStart) / 2;
            if (matrix[row][mid] == target) {
                return new int[]{row, mid};
            }
            if (matrix[row][mid] < target) {
                colStart = mid + 1;
            } else {
                colEnd = mid - 1;
            }
        }
        return new int[]{-1, -1}; // Not found
    }

    static int[] search(int[][] matrix, int target) {
        int rows = matrix.length;
        if (rows == 0) return new int[]{-1, -1}; // Edge case: empty matrix
        int cols = matrix[0].length;

        // Binary search on rows
        int rowStart = 0;
        int rowEnd = rows - 1;

        while (rowStart <= rowEnd) {
            int mid = rowStart + (rowEnd - rowStart) / 2;
            if (matrix[mid][0] <= target && matrix[mid][cols - 1] >= target) {
                // Target may be in this row
                return binarySearch(matrix, mid, 0, cols - 1, target);
            } else if (matrix[mid][0] > target) {
                rowEnd = mid - 1;
            } else {
                rowStart = mid + 1;
            }
        }
        return new int[]{-1, -1}; // Not found
    }
}

    

