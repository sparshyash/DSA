def reverseArray(arr):
    
    # Initialize left to the beginning and right to the end
    left = 0
    right = len(arr) - 1
  
    # Iterate till left is less than right
    while left < right:
        
        # Swap the elements at left and right position
        arr[left], arr[right] = arr[right], arr[left]
      
        # Increment the left pointer
        left += 1
      
        # Decrement the right pointer
        right -= 1
        
        
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    
    reverseArray(arr)
    
    print("Reversed array:", arr)
    
Array Rotations is a transformation where the array is rotated k times to the right or left, causing elements to shift cyclically. This operation can be done efficiently in-place.

To rotate the array, reverse the last k elements, reverse the first n − k elements, and finally reverse the entire array.



def rotateclockwise(arr, k):
    n = len(arr)
    if n == 0:
        return

    k = k % n

    # Reverse last k elements
    arr[n - k:] = reversed(arr[n - k:])

    # Reverse first n-k elements
    arr[:n - k] = reversed(arr[:n - k])

    # Reverse the entire array
    arr[:] = reversed(arr)

    # No return — modifies arr in-place
    
