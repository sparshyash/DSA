s1 = 'GfG'  
s2 = "GfG"  
print(s1)
print(s2)

s = "GeeksforGeeks"
print(s[0])   
print(s[4])

s = "GeeksforGeeks"
print(s[-10])  
print(s[-5]) # Accessing with negative indexes 

# STRING SLICING

s = "GeeksforGeeks"
print(s[1:4])    
print(s[:3])     
print(s[3:])    # Triming
# Reverse String 
print(s[::-1])   

s = "Python"
for char in s:
    print(char)

s = "geeksforGeeks"
s = "G" + s[1:]   # Strings are immutable 
print(s)

s = "GfG"
del s

s = "hello geeks"
s1 = "H" + s[1:]                  
s2 = s.replace("geeks", "GeeksforGeeks")  
print(s1)
print(s2)  # This creates new string as strings are immutable 


s = "GeeksforGeeks"
print(len(s))

s = "Hello World"
print(s.upper())    # UpperCase
print(s.lower())  # Lowercase

s = "   Gfg   "
print(s.strip())    # remove leading and trailing whitespaces

s = "Python is fun"
print(s.replace("fun", "awesome"))

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

s = "Hello " 
print(s * 3)

name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")  # F - strings

s = "My name is {} and I am {} years old.".format("Alice", 22) 
print(s)

a=False
b=True

print(f"{str(a and b).lower()} {str(a or b).lower()} {str(not a).lower()}")

s = "GeeksforGeeks" 
print("Geeks" in s) 
print("GfG" in s)    # String membership 



test=1234

print(f"Binary representation of {test} is {bin(test)}")

print(f"Octal representation of {test} is {oct(test)}")

print(f"Hexadecimal representation of {test} is {hex(test)}")

print(f"Decimal representation of {test} is {int(test)}")

print(f"String representation of {test} is {str(test)}")

print("".join(reversed(str(test))))


# Broadcasting in NumPy describes how arithmetic operations treat arrays of different shapes during element-wise calculations. It allows a smaller array to be virtually "stretched" across a larger array so they have compatible shapes, without making redundant copies of data in memory.

# The General Broadcasting Rule
# When operating on two arrays, NumPy compares their shapes element-wise, starting with the trailing (rightmost) dimensions and working its way left.

# Two dimensions are compatible if:

# They are equal, or

# One of them is 1.

# If either array has fewer dimensions than the other, its shape is prepended with 1s on the left until both shapes have the same length. If the dimensions do not satisfy these conditions, NumPy raises a ValueError: operands could not be broadcast together.

# Common Scenarios
# 1. Scalar and 1D Array
# The scalar is treated as having shape (1,) and stretched across the array.

# Plaintext
# A:      (3,)       -> [10, 20, 30]
# B:       ()  (scalar 2)
# Result: (3,)       -> [12, 22, 32]
# 2. 2D Array and 1D Array
# The 1D array is aligned to the trailing dimension (columns) and stretched across all rows.

# Plaintext
# A:      (3, 3)
# B:         (3,)  --> padded to (1, 3) --> stretched to (3, 3)
# Result: (3, 3)
# 3. Row Vector and Column Vector
# Both arrays stretch along the dimension where their size is 1, producing an outer operation.

# Plaintext
# A:      (3, 1)   --> stretched to (3, 4)
# B:      (1, 4)   --> stretched to (3, 4)
# Result: (3, 4)
# 4. Incompatible Shapes (Throws Error)

# Plaintext
# A:      (3, 2)
# B:      (3, 3)
# Trailing dimensions (2 and 3) do not match and neither is 1. -> ValueError
# Code Example
# Python
import numpy as np

# Shape (3, 1)
col_vec = np.array([[1], 
                    [2], 
                    [3]])

# Shape (1, 4)
row_vec = np.array([[10, 20, 30, 40]])

# Broadcasting produces shape (3, 4)
result = col_vec + row_vec

print("Result shape:", result.shape)
print(result)
# Output:
# [[11 21 31 41]
#  [12 22 32 42]
#  [13 23 33 43]]