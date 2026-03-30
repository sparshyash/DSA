import math

def printDivisors(n):
    divisors = []
    
    # Loop runs up to square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            
            # If both divisors are same (perfect square), add only once
            if n // i == i:
                divisors.append(i)
            else:
                
                # Add both divisors
                divisors.append(i)
                divisors.append(n // i)
    return divisors

if __name__ == "__main__":
    number = 10
    divisors = printDivisors(number)

    for div in divisors:
        print(div, end=" ")