# Find all prime from 1 to n



import math

# Approach 1   -- for each i check if i / y any of 2 to i-1  O(n^2)
def isPrime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return  True


def sieve(n):
    res = []

    for i in range(2, n + 1):
        if isPrime(i):
            res.append(i)

    return res


if __name__ == "__main__":
    n = int(input("Enter the value of n: "))

    res = sieve(n)

    for ele in res:
        print(ele, end=' ')


# approach 2 -> Seive of Erastothenes  O(nloglogn)



