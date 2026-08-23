# function to convert decimal to binary

# Approach 1 O(n) as time and O(logn) as space  
def decToBinary(n):
    binArr = []

    while n > 0:
        bit = n % 2
        binArr.append(str(bit))
        n //= 2

    # reverse the string
    binArr.reverse()
    return "".join(binArr)


# using recursion :  Using Head Recursion - O(log₂(n)) Time and O(log₂(n)) Space
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


# Using Bitwise Operators - O(log₂(n)) Time and O(log₂(n)) Space
# Using bitwise operators, we can extract binary digits by checking the least significant bit (n & 1) and then right-shifting the number (n >> 1) to process the next bit.
# This method is faster than arithmetic division and modulo, as bitwise operations are more efficient at the hardware level.


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

# Using Built-in Methods - O(log₂(n)) Time and O(log₂(n)) Space
# The main idea is to leverage built-in functions provided by programming languages to directly convert a decimal number to its binary form. These functions abstract away the underlying logic and return the binary representation as a string, making the process quick, concise, and error-free.

import math

def decToBinary(n):
	return bin(n)[2::]  # o/p is 0b1001 hence start from 2
  
if __name__ == "__main__":
    n = 12
    print(decToBinary(n))

