class solution(object):
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine the sign of the integer
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the absolute value of the integer
        reversed_num = 0
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
            
        # Reapply the sign
        result = sign * reversed_num
        
        # Check for 32-bit overflow
        if result < INT_MIN or result > INT_MAX:
            return 0
            
        return result
    def main():
        x=-123
        print(solution().reverse(x))