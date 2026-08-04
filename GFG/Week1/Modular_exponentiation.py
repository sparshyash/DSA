def powMod(x, n, M):
    res = 1

    # loop from 1 to n
    for _ in range(n):
                
        # Multiplying res with x
        # and taking modulo to avoid overflow
        res = (res * x) % M
    return res

if __name__ == "__main__":
    x, n, M = 3, 2, 4
    print(powMod(x, n, M))
    
    
    
# Approach2  O(log n) time complexity

def powMod(x, n, M):
    res = 1

    # Loop until exponent becomes 0
    while n >= 1:
        
        # n is odd, multiply result by current x and take modulo
        if n % 2 == 1:
            res = (res * x) % M
            
            # Make n even
            n -= 1 
        else:
            
            # n is even, square the base and halve the exponent
            x = (x * x) % M
            n //= 2

    return res

if __name__ == "__main__":
    x, n, M = 3, 2, 4
    print(powMod(x, n, M))

