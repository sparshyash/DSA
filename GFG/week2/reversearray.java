package GFG.week2;

public class reversearray {

public void reverseArray(int[] arr) {
        
    // Initialize left to the beginning and right to the end
    int left = 0, right = arr.length - 1;

    // Iterate till left is less than right
    while (left < right) {
        
        // Swap the elements at left and right position
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;

        // Increment the left pointer
        left++;

        // Decrement the right pointer
        right--;
    }
} 

}
