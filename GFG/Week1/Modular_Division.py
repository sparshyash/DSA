def modInverse(n, m):
    
    # BASIC 

    # Try all values from 1 to m-1
    for x in range(1, m):
        
        # Check if (n * x) % m == 1.
        # Note that n and x can be larger
        # than m, so we do modulo before
        # mulityplying
        if ((n *x)%m == 1):
            return x

    return -1

if __name__ == "__main__":
    n = 2
    m = 13

    print(modInverse(n, m))
    
    
# Approach 2

# Python program to demonstrate working of 
# extended Euclidean Algorithm 

# Function to return
# gcd of a and b
def findGCD(a, b):
    if a == 0:
        return b
    return findGCD(b % a, a)

# Main function
def main():
    a, b = 35,15
    g = findGCD(a,b)
    
    print(g)

if __name__ == "__main__":
    main()
    


# Binary exponentiation
def power(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# function to calculate GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modInverse(b, m):
    return power(b, m - 2, m)

def modDivide(a, b, m):
    
     # Division not possible
    if b == 0 or gcd(b, m) != 1:
        return -1
    invmodm = modInverse(b, m)
    return (a %m * invmodm) % m

if __name__ == "__main__":
    a, b, m = 10, 2, 13
print(modDivide(a, b, m))




#Approach 2   Extended Euclidean Algorithm O(log M) Time and O(1) Space
#  To find the modular inverse of a number b modulo M using the Extended Euclidean Algorithm, we aim to solve the equation b * x + M * y = gcd(b, M). If the greatest common divisor gcd(b, M) is 1, then x is the modular inverse of b modulo M. The Extended Euclidean Algorithm computes both gcd and the coefficients x and y that satisfy this linear combination. Once x is found, we take its positive equivalent by calculating (x % M + M) % M to get the correct modular inverse. This approach works for any modulus M, not necessarily prime.




def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Compute modular inverse
def modInverse(b, M):
    gcd, x, _ = gcdExtended(b, M)
    if gcd != 1:
        return -1
    return (x % M + M) % M

# Perform (a / b) % M
def modDivide(a, b, M):
    a %= M
    inv = modInverse(b, M)
    if inv == -1:
        return -1
    return (a * inv) % M

if __name__ == "__main__":
    a = 10
    b = 2
    M = 13
    result = modDivide(a, b, M)
    print(result)