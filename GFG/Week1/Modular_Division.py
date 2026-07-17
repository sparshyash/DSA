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
    inv = modInverse(b, m)
    return (a * inv) % m

if __name__ == "__main__":
    a, b, m = 10, 2, 13
print(modDivide(a, b, m))