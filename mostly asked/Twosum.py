# method 1  O(n^2)

def Twosumloops(arr,target):
    i=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]+arr[i]==target:
                return [i,j]
            
    return [-1,-1]

# method 2 O(nlogn) two pointer approach

def Twosumtwopointer(arr,target):
    
    left=0
    right=len(arr)-1
    while left < right:
        if arr[left] + arr[right] == target:
            return [left,right]
        elif arr[left] + arr[right] < target:
            left+=1
        else:
            right-=1
    return [-1,-1]

# method 3 O(n) using hashmap

def Twosumhashmap(arr,target):
    hashmap={}  # store numbers seen so far with index as value
    for i in range(len(arr)):
        complement=target-arr[i]
        if complement in hashmap:
            return [hashmap[complement],i]
        hashmap[arr[i]]=i
    return [-1,-1]

if __name__ == "__main__":
    n=5
    arr=[2,3,4,5]
    target=9
    ans=Twosumhashmap(arr,target)
    print("This is the answer for variant 3:", ans)
    ans2=Twosumtwopointer(arr,target)
    print("This is the answer for variant 2:", ans2)
    ans3=Twosumloops(arr,target)
    print("This is the answer for variant 1:", ans3)
    
    