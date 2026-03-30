# function to convert decimal to binary
def decToBinary(n):
    binArr = []

    while n > 0:
        bit = n % 2
        binArr.append(str(bit))
        n //= 2

    # reverse the string
    binArr.reverse()
    return "".join(binArr)

def decToBinaryRec(n, binArr):
    # Base Case
    if n == 0:
        return
    
    # Recur for smaller bits.
    decToBinaryRec(n // 2, binArr)
    
    # Add MSB of current number to the binary list
    binArr.append(str(n % 2))

# Function to convert decimal to binary
def decToBinary(n):
    if n == 0:
        return "0"

    binArr = []
    decToBinaryRec(n, binArr)
    return "".join(binArr)

def decToBinary(n):
  
    # String to store the binary representation
    bin = ""

    while n > 0:
        # Finding (n % 2) using bitwise AND operator
        # (n & 1) gives the least significant bit (LSB)
        bit = n & 1
        bin += str(bit)

        # Right shift n by 1 (equivalent to n = n // 2)
        # This removes the least significant bit (LSB)
        n = n >> 1

    return bin[::-1]

