package GFG.week2;

public class reversearraywithpointers {

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


Array Rotations is a transformation where the array is rotated k times to the right or left, causing elements to shift cyclically. This operation can be done efficiently in-place.

To rotate the array, reverse the last k elements, reverse the first n − k elements, and finally reverse the entire array.

