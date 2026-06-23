# Find all prime from 1 to n 

# Approach 1   -- for each i check if i / y any of 2 to i-1  O(n^2)
def approach1(n):
    primes=[]
    for i in range(2,n+1):
        isprime=True
        for j in range(2,i-1):
            if i%j==0:
                isprime=False
                
                break

        if isprime:
            primes.append(i)
    return primes


# approach 2 -> Seive of Erastothenes  O(nloglogn)

def approach2(n):
    primes=[True]*(n+1)
    primes[0]=primes[1]=False
    for i in range(2,n+1):
        if primes[i]:
            for j in range(i*i,n+1,i):
                primes[j]=False
    return [i for i in range(2,n+1) if primes[i]]