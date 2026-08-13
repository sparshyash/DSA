import java.util.Arrays;
import java.util.*;

class Solution {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6};
        ArrayList<Integer> list = new ArrayList<Integer>();

        // Step 1: Store the first 3 elements in the list
        for (int i = 0; i < 3; i++) {
            list.add(arr[i]);
        }

        // Step 2: Shift the remaining elements of the array
        for (int i = 0; i < 3; i++) {
            arr[i] = arr[3 + i];
        }

        // Step 3: Restore the original first 3 elements from the list
        for (int i = 0; i < 3; i++) {
            arr[3 + i] = list.get(i);
        }

        // Output the modified array
        System.out.println(Arrays.toString(arr));
    }

    public static String read(int n, int[] book, int target) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'read'");
    }
}
