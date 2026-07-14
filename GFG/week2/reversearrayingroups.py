def reversearray(arr , k):
    n=len(arr)
    i=0
    
    while i<n:
        left=i
        
        right=min(i+k-1,n-1)

        while left < right :
            arr[left],arr[right]=arr[right],arr[left]
            
            left+=1
            right-=1
    
        i+=k
    return arr

if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8]
    
    print(reversearray(arr ,3))
    