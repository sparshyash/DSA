def mooresvoting(arr):
    count = 0
    cand = 0
    for num in arr:
        # new candidate
        if count == 0:
            cand = num  
        # vote count
        count += 1 if num == cand else -1  
    return cand

if __name__ == "__main__":
    arr = [1,2,3,4,4,4]
    print(mooresvoting(arr))  # Output: 4