
# Using Standard Division with Sign Correction O(1) Time and O(1) Space

def floorDiv(a, b):
    
    # Python's // operator gives correct floor division
    return a // b

# Method to compute ceil of a / b
def ceilDiv(a, b):
    
    # Flip signs to force ceiling behavior
    return -(-a // b)

# Method to compute both floor and ceil of a / b
def divFloorCeil(a, b):
    res = []
    res.append(floorDiv(a, b))
    res.append(ceilDiv(a, b))
    return res

if __name__ == "__main__":
    a, b = -7, 2
    res = divFloorCeil(a, b)
    print(res[0], res[1])
    




# Using built-in functions O(1) Time and O(1) Space
# Use built-in math functions (floor and ceil) to directly compute the greatest integer ≤ a/b and the smallest integer ≥ a/b, ensuring correct rounding behavior for both positive and negative values.

import math

# Function to compute and return both 
# floor and ceil of a / b
def divFloorCeil(a, b):
    
    # Compute floor(a / b) using built-in math.floor
    floor_val = math.floor(a / b)
    
    # Compute ceil(a / b) using built-in math.ceil
    ceil_val = math.ceil(a / b)
    
    return [floor_val, ceil_val]


if __name__ == "__main__":
    a, b = -7, 2
    
    res = divFloorCeil(a, b)
    
    print(res[0], res[1])
    
    