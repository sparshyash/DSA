def twosum(arr , target):
    hashmap={}  # store numbers seen so far with index as value
    for i in range(len(arr)):
        complement=target-arr[i]
        if complement in hashmap:
            return [hashmap[complement],i]
        hashmap[arr[i]]=i
    return [-1,-1]

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    result = twosum(numbers, target)
    print("Indices: [{}]".format(", ".join(map(str, result))))