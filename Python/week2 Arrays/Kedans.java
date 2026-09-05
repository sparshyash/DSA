public class Kedans {
    
    static int kedan(int arr[]) {
        // Edge case: if the array is empty
        if (arr == null || arr.length == 0) {
            return 0; 
        }
            // sliding window
        int currentMax = arr[0]; // Tracks the max sum ending at the current position
        int res = arr[0];  // Tracks the overall maximum sum found so far
        
        // Start from index 1 since index 0 is already used for initialization
        for (int i = 1; i < arr.length; i++) {
            // Decide whether to add the current element to the existing subarray 
            // or start a brand new subarray from the current element
            currentMax = Math.max(arr[i], currentMax + arr[i]);
            
            // Update the global maximum if the current subarray sum is better
            res = Math.max(res, currentMax);
        }
        
        return res;
    }
    
    public static void main(String[] args) {
        int arr[] = {1, 2, 3, -8, 2, 4};
        int ans = kedan(arr);
        System.out.println(ans); // Output will be 6 (from the subarray {1, 2, 3})
    }

}



