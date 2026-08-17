def nextpermutation(arr):
    n=len(arr) 
    
    i=n-2
    # find 1st dec from right
    
    while i>=0  and arr[i] >= arr[i+1]:
        i-=1
    # if entire array is desc , i will be -1
    if i>=0:
        j=n-1
        while arr[j]<=arr[i]:
            j-=1
            
            arr[i],arr[j] =arr[j],arr[i]
    arr[i+1:] = reversed(arr[i+1:])
    
    
if __name__=="__main__":
    arr=[1,2,3]
    nextpermutation(arr)
    print(arr)  # Output: [1, 3, 2]