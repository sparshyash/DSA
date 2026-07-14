import java.util.ArrayList;

public class spiraltraversal {
    ArrayList<Integer> spirallyTraverse(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;

        ArrayList<Integer> res = new ArrayList<>();

        // Initialize boundaries
        int top = 0, bottom = m - 1, left = 0, right = n - 1;

        // Iterate until all elements are Stored
        while (top <= bottom && left <= right) {

            // Store top row from left to right
            for (int i = left; i <= right; ++i) {
                res.add(mat[top][i]);
            }
            top++;

            // Store right column from top to bottom
            for (int i = top; i <= bottom; ++i) {
                res.add(mat[i][right]);
            }
            right--;

            // Store bottom row from right to left (if exists)
            if (top <= bottom) {
                for (int i = right; i >= left; --i) {
                    res.add(mat[bottom][i]);
                }
                bottom--;
            }

            // Store left column from bottom to top (if exists)
            if (left <= right) {
                for (int i = bottom; i >= top; --i) {
                    res.add(mat[i][left]);
                }
                left++;
            }
        }

        return res;
    }
}
