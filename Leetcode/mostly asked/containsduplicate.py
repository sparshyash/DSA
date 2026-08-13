def containsduplicate(arr):
    n=len(arr)
    hashmap={}
    for i in range(n):
        if arr[i] in hashmap:
            return True
        
        hashmap[arr[i]] = True
    return False
def containsduplicateset(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
if __name__ == "__main__":
    arr=[1,2,3,4,5,2]
    ans=containsduplicate(arr)
    print(ans)
    ans=containsduplicateset(arr)
    print(ans)