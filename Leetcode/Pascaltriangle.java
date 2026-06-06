

import java.util.*;

public class Pascaltriangle {
    public static ArrayList<ArrayList<Long>> printPascal(int n) {
        // Initialize the result to store rows of Pascal's Triangle
        ArrayList<ArrayList<Long>> result = new ArrayList<>();
        
        // Handle the case where N is 0 (no rows to generate)
        if (n == 0) return result;
        
        // The first row is always [1]
        ArrayList<Long> firstRow = new ArrayList<>();
        firstRow.add(1L);  // Use Long instead of Integer
        result.add(firstRow);
        
        // For subsequent rows
        for (int i = 1; i < n; i++) {
            ArrayList<Long> currentRow = new ArrayList<>();
            
            // Add 1 at the start of each row
            currentRow.add(1L);
            
            // Fill the middle values of the row
            for (int j = 1; j < i; j++) {
                long sum = result.get(i - 1).get(j - 1) + result.get(i - 1).get(j);
                currentRow.add(sum);
            }
            
            // Add 1 at the end of each row
            currentRow.add(1L);
            
            // Add the current row to the result
            result.add(currentRow);
        }
        
        return result;
    }
    // Function to print the 2D ArrayList (Pascal's Triangle)
    public static void printPascalsTriangle(ArrayList<ArrayList<Long>> triangle) {
        for (ArrayList<Long> row : triangle) {
            for (long num : row) {
                System.out.print(" "+ num + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        // Example usage
        int n = 5;  // Example: generate Pascal's Triangle for the first 5 rows
        ArrayList<ArrayList<Long>> triangle = printPascal(n);
        printPascalsTriangle(triangle);
    }
}
