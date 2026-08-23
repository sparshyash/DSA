# O(1) time and space


def isEven(n):
    
    # finding remainder of n
    rem = n % 2; 
    if rem == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = 15
    if isEven(n):
        print("true")
    else:
        print("false")
        
#  using bitwise and ooperator 

# Using Bitwise AND Operator - O(1) Time and O(1) Space
# The last bit of all odd numbers is always 1, while for even numbers it’s 0. So, when performing bitwise AND operation with 1, odd numbers give 1, and even numbers give 0.

# Note: Bitwise operators are extremely fast and efficient because they operate directly at the binary level, making them significantly faster than arithmetic or logical operations.


def isEven(n):
    # taking bitwise and of n with 1 
    if (n & 1) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = 15
    if isEven(n):
        print("true")
    else:
        print("false")
        
