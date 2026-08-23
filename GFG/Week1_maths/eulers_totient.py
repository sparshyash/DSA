# Given an integer n, find the value of Euler's Totient Function, denoted as Φ(n). The function Φ(n) represents the count of positive integers less than or equal to n that are relatively prime to n.

# Euler's Totient function Φ(n) for an input n is the count of numbers in {1, 2, 3, ..., n-1} that are relatively prime to n, i.e., the numbers whose GCD (Greatest Common Divisor) with n is 1.

# If n is a positive integer and its prime factorization is; 

# n=p^e1...pk^eK 

# ϕ(n) = n.(1-1/p1)...(1-1/p^k)

# [Naive Approach] Iterative GCD Method  O(n)
# A simple solution is to iterate through all numbers from 1 to n-1 and count numbers with gcd with n as 1. Below is the implementation of the simple method to compute Euler's Totient function for an input integer n. 


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

# A simple method to evaluate Euler Totient Function 
def etf(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result

Time Complexity: O(n log n)
Auxiliary Space: O(log min(a,b)) where a,b are the parameters of gcd function.

[Expected Approach] Euler’s Product Formula
The idea is based on Euler's product formula which states that the value of totient functions is below the product overall prime factors p of n. 

Phi(n)= n *pi i = p to n (1 -1 /p)

1) Initialize result as n
2) Consider every number 'p' (where 'p' varies from 2 to Φ(n)). 
   If p divides n, then do following
   a) Subtract all multiples of p from 1 to n [all multiples of p
      will have gcd more than 1 (at least p) with n]
   b) Update n by repeatedly dividing it by p.
3) If the reduced n is more than 1, then remove all multiples
   of n from result.


def etf(n):
    
    result = n

    # Consider all prime factors of n 
    # and subtract their multiples 
    # from result
    p = 2
    while p * p <= n:
        
        if n % p == 0:
            while n % p == 0:
                n //= p

            result -= result // p
        p += 1

    # If n has a prime factor greater than sqrt(n)
    # (There can be at-most one such prime factor)
    if n > 1:
        result -= result // n

    return result
    
 
# Time Complexity: O(√n)
# Auxiliary Space: O(1)

Some Interesting Properties of Euler's Totient Function 
1) For a prime number p, 

ϕ(p)=p−1

2) For two prime numbers a and b          
 ϕ(a⋅b)=ϕ(a)⋅ϕ(b)=(a−1)⋅(b−1)           , used in RSA Algorithm
 
3) For a prime number p and integer k ≥ 1:

ϕ(pk) = p ^ k−p ^ k  − 1

4) Special Case : gcd(a, b) = 1


ϕ(a⋅b)=ϕ(a)⋅ϕ(b)⋅  1 / ϕ(1) =ϕ(a)⋅ϕ(b).

5) Sum of values of totient functions of all divisors of n is equal to n. 
 
symmation sign d to n phi (d) = n

n = 6 , factors = {1, 2, 3, 6}
n = ϕ(1)+ϕ(2)+ϕ(3)+ϕ(6) = 1 + 1 + 2 + 2 = 6

The most famous and important feature is expressed in Euler's theorem : 

The theorem states that if n and a are coprime
(or relatively prime) positive integers, then

aΦ(n) Φ 1 (mod n) 

The RSA cryptosystem is based on this theorem:
In the particular case when m is prime say p, Euler's theorem turns into the so-called Fermat's little theorem : 

ap-1 Φ 1 (mod p) 

