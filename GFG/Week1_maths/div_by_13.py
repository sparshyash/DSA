def isdivby13(s):
    num=int(s) # typecasting

    return num%13==0

Time Complexity: O(n), n is length of s
Auxiliary Space: O(1)

Alternating Sum of 3-Digit Blocks
A number is divisible by 13 if and only if the alternating sum of its 3-digit blocks, taken from right to left, is divisible by 13.

Step by Step approach -

Pad the number so its length is a multiple of 3
-> If the number of digits is not a multiple of 3, append zeros to the right so each block has exactly 3 digits.
-> Example: "2911285" → "291128500" (after padding with two zeros).
Split into 3-digit blocks from right to left
-> Example: "291128500" → blocks: 500, 128, 291 (right to left order).
Apply alternating signs starting with + on the rightmost block
-> Pattern from right to left: + block , - block, + block, …
-> Example: +500 - 128 + 291.
Sum the results
-> Example: 500 - 128 + 291 = 663.
Check divisibility by 13
-> If the sum is divisible by 13, the original number is divisible by 13.
-> Example: 663 % 13 == 0 → divisible.




def divBy13(s):
    length = len(s)
​
    # Special case: if the number is "0"
    if length == 1 and s[0] == '0':
        return True
​
    # Make the length a multiple of 3 by padding zeros at the end
    if length % 3 == 1:
        s += "00"
        length += 2
    elif length % 3 == 2:
        s += "0"
        length += 1
​
    sum_ = 0
    p = 1
​
    # Traverse from right to left in steps of 3 digits
    i = length - 1
    while i >= 0:
        group = 0
        group += int(s[i])
        i -= 1
        group += int(s[i]) * 10
        i -= 1
        group += int(s[i]) * 100
        i -= 1
​
        sum_ += group * p
        p *= -1
​
    sum_ = abs(sum_)
    return sum_ % 13 == 0
​
if __name__ == "__main__":
    s = "2911285"
    isDivisible = divBy13(s)
    
    if isDivisible:
        print("true")
    else:
        print("false")

Output
true
Time Complexity: O(n), n is length of s
Auxiliary Space: O(1)


 String-Based Modulo
We process the number digit by digit from left to right, maintaining the remainder modulo 13 at each step using the formula:
rem = (rem * 10 + digit) % 13.

Step by Step Approach -

Initialize remainder:
-> rem = 0
Process each digit from left to right:
-> Digit '2': rem = (0 * 10 + 2) % 13 = 2
-> Digit '9': rem = (2 * 10 + 9) % 13 = 29 % 13 = 3
-> Digit '1': rem = (3 * 10 + 1) % 13 = 31 % 13 = 5
-> Digit '1': rem = (5 * 10 + 1) % 13 = 51 % 13 = 12
-> Digit '2': rem = (12 * 10 + 2) % 13 = 122 % 13 = 5
-> Digit '8': rem = (5 * 10 + 8) % 13 = 58 % 13 = 6
-> Digit '5': rem = (6 * 10 + 5) % 13 = 65 % 13 = 0
Since final rem = 0, the number 2911285 is divisible by 13.




def divBy13(s):
​
    # Stores running remainder
    rem = 0  
​
    # Process each digit and compute remainder modulo 13
    for ch in s:
        rem = (rem * 10 + int(ch)) % 13
​
    # Final check for divisibility
    return rem == 0
​
if __name__ == "__main__":
    s = "2911285"
    
    if divBy13(s):
        print("true")
    else:
        print("false")

Output
true
Time Complexity: O(n), n is length of s
Auxiliary Space: O(1)


    