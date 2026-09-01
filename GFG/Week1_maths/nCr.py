# Approach 1 O(2^n) and O(n) space complexity  -> exponential


def nCr1(n, r):  # nCr=n! / (r! * (n-r)!)
   
    # No valid combinations if r is greater than n
    if r > n:  
        return 0
   
    # Base case: only one way to choose 0 or all elements    
    if r == 0 or r == n:  
        return 1
   
    # include or exclude current element
    return nCr(n - 1, r - 1) + nCr(n - 1, r)  # nCr= n-1Cr-1 + n-1Cr



i
    
    
# Approach 2 O(n) time complexity and O(n) space complexity using factorial 

# This approach calculates the nCr using the factorial formula. It first computes the factorial of a given number by multiplying all integers from 1 to that number. 
# To find  nCr, it calculates the factorial of n, r, and (n - r) separately, 
# then applies the formula n! / (r!(n-r)!) to determine the result. Since factorial values grow rapidly, 
# this method is inefficient for large values due to integer overflow and excessive computations. 

# Driver Code



def Multiplier(start, end):
    if start == end:
        return start
    res = 1
    while start <= end:
        res *= start
        start += 1
    return res

def nCr(n, r):
    # No valid combinations if r > n
    if n < r:  
        return 0
    # Base cases: nC0 or nCn = 1
    if n == r or r == 0:  
        return 1

    # Use max(r, n - r) to reduce 
    # number of multiplications
    max_val = max(r, n - r)
    min_val = min(r, n - r)

    nume = Multiplier(max_val + 1, n)
    deno = Multiplier(1, min_val)
    return nume // deno


# Approach 3 Using By using Binomial Coefficient formula - O(r) Time and O(1) Space

# A binomial coefficient C(n, k) can be defined as the coefficient of X ^ k in the expansion of (1 + X)n.
# A binomial coefficient C(n, k) also gives the number of ways, disregarding order, 
# that k objects can be chosen from among n objects; more formally, the number of k-element subsets
# (or k-combinations) of an n-element set.
# Iterative way of calculating nCr   using binomial coefficient formula.

# nCr = n! / r! * (n-r)! = n * n-1*...*n-r+1 / r! =  pi i = 1 to r  n*n-1*n-2...n-r+1 / i

def nCr(n, r):
    
    sum = 1

    # Calculate the value of n choose r 
    # using the binomial coefficient formula
    for i in range(1, r+1):
        sum = sum * (n - r + i) // i
    
    return sum



# [Alternate Approach] Using Logarithmic Formula - O(r) Time and O(1)
# Logarithmic formula for nCr is an alternative to the factorial formula that avoids computing factorials directly and it's more efficient for large values of n and r. It uses the identity log(n!) = log(1) + log(2) + ... + log(n) to express the numerator and denominator of the nCr in terms of sums of logarithms which allows to calculate the nCr using the Logarithmic operations. This approach is faster and very efficient.
# The logarithmic formula for nCr is: nCr = exp( log(n!) - log(r!) - log((n-r)!))


#   nCr == n*n-1*...n-r + 1 / r! == pi i = 0 to r -1  n-i / i + 1
# taking log --> log(nCr) == summation i =1 to r-1 ( log n-i) -log(i+1)


def nCr(n, r):
     # Invalid case
    if r > n:                 
        return 0
    # Base cases
    if r == 0 or n == r:       
        return 1

    res = 0
    for i in range(r):
        # log(n!) - log(r!) - log((n-r)!)
        res += math.log(n - i) - math.log(i + 1)  

    return round(math.exp(res))  
    
    
if __name__ == "__main__":
    n = 5
    r = 2
    print(nCr1(n, r))

