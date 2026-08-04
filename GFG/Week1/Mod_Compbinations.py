# Approach 1 O(2^n) and O(n) space complexity  -> exponential


def nCr(n, r):
   
    # No valid combinations if r is greater than n
    if r > n:  
        return 0
   
    # Base case: only one way to choose 0 or all elements    
    if r == 0 or r == n:  
        return 1
   
    # include or exclude current element
    return nCr(n - 1, r - 1) + nCr(n - 1, r)

# Driver Code
if __name__ == "__main__":
    n = 5
    r = 2
    print(nCr(n, r))
    


#Approach 2 O(n)

