def rotatearr(arr ,k):
    n=len(arr)
    k=k%n
    
    
    arr[:n-k] = reversed(arr[:n-k])
    
    arr[n-k:] = reversed(arr[n-k:])
    
    arr[:]  = reversed(arr)
    return arr

if __name__=="__main__":
    arr=[1,2,3,4,5,6]
    k=2
    ans=rotatearr(arr,k)
    print(ans)