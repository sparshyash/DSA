def subarraysum(arr):
    n=len(arr)
    res=0
    maxfind=0
    
    for i in range(len(arr)):
        maxfind = max(arr[i],maxfind+arr[i])
        
        res=max(res,maxfind)
        
    return res

if __name__=="__main__":
    arr = [1,2,3,4,5,6,-2,-8,-23,3,4,5,2]
    ans=subarraysum(arr)
    
    print(ans)