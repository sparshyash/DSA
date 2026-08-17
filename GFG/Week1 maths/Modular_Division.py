#  Using Fermats little theorem to find modular division

# If the modulus m is a prime number, we can use Fermat’s Little Theorem to find the modular inverse of b. 
# According to the theorem, the inverse of b modulo m is b M-2 % M. So we can use Modular Exponentiation for computing 
# b M-2 % M.

# Binary exponentiation
def power(base, exp, mod):
    result = 1
    base %= mod  #  taki out of bound na ho jae isliye phle divide kr dete hai 
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2  # kyoki hum ab hum multiply kr chuke hai to ab hum exp ko half kr denge
    return result

# function to calculate GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modInverse(b, m):
    return power(b, m - 2, m)

def modDividefermit(a, b, m):
    
    # Division not possible
    if b == 0 or gcd(b, m) != 1:
        return -1
    inv = modInverse(b, m)
    return (a * inv) % m   # wroks only when M is prime since gcd (b,m) = 1 is not guaranteed for non-prime M



# Method 2: Using Extended Euclidean Algorithm

# To find the modular inverse of a number b modulo M using the Extended Euclidean Algorithm,
# we aim to solve the equation b * x + M * y = gcd(b, M). If the greatest common divisor gcd(b, M) is 1, 
# then x is the modular inverse of b modulo M. The Extended Euclidean Algorithm computes both gcd and the coefficients
# x and y that satisfy this linear combination. Once x is found, we take its positive equivalent by calculating (x % M + M) % M to get
# the correct modular inverse. This approach works for any modulus M, not necessarily prime.


# Extended Euclidean Algorithm
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
    return (x % M + M) % M  # addition hum negative no k  lioye krte hai 

# Perform (a / b) % M
def modDivideeuclidean(a, b, M):
    a %= M
    inv = modInverse(b, M)
    if inv == -1:
        return -1
    return (a * inv) % M









if __name__ == "__main__":
    a, b, m = 10, 2, 13
print(modDividefermit(a, b, m))
print(modDivideeuclidean(10, 3,4))


