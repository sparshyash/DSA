import java.util.Arrays;

public class LinearSearch1D {
    public static void main(String[] args) {
        int[] name = {1, 2, 2, 3, 4, 5, 2};
        int ans = -1;
        int target = 2;
        boolean findLast = true;

        for (int i = 0; i < name.length; i++) {
            if (name[i] == target) {
                ans = i;
                if (!findLast) {
                    break;
                }
            }
        }

        if (ans != -1) {
            System.out.println("Target found at index: " + ans);
        } else {
            System.out.println("Target not found.");
        }
    }
}
