import java.util.HashMap;

public class Twosum {
    public static int[] twoSumloops(int n, int []arr, int target) {
        int[] ans = new int[2];
        ans[0] = ans[1] = -1;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[i] + arr[j] == target) {
                    ans[0] = i;
                    ans[1] = j;
                    return ans;
                }
            }
        }
        return ans;

         
    }

    public static int[] twosumtwopointer(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        while (left < right) {
            int sum = arr[left] + arr[right];
            if (sum == target) {
                return new int[]{left, right};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[]{-1, -1};
    }

    public static int[] twosumhashmap(int[] arr, int target) {
        HashMap<Integer, Integer> hashmap = new java.util.HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            int complement = target - arr[i];
            if (hashmap.containsKey(complement)) {
                return new int[]{hashmap.get(complement), i};
            }
            hashmap.put(arr[i], i);
        }
        return new int[]{-1, -1};
    }

    public static void main(String args[]) {
        int n = 5;
        int[] arr = {2, 6, 5, 8, 11};
        int target = 17;
        int[] ans = twoSumloops(n, arr, target);
        System.out.println("This is the answer for variant 2: [" + ans[0] + ", "
                           + ans[1] + "]");

        ans=twosumtwopointer(arr,target);
        System.out.println("This is the answer for variant 3: [" + ans[0] + ", "
                           + ans[1] + "]");
        ans=twosumhashmap(arr,target);
        System.out.println("This is the answer for variant 4: [" + ans[0] + ", "
                           + ans[1] + "]");
    }

}