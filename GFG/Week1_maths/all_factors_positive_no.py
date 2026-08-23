import math

# Approach 1 O(n) as it iterates from 1 to n

def getDivisors(n):
    
    # Create a list to store divisors
    divisors = []

    # Iterate from 1 to n and check divisibility
    for i in range(1, n + 1):
        if n % i == 0:
            
            # If 'i' divides 'n' evenly, it's a divisor
            divisors.append(i)

    return divisors



        

# Approach 2 O(sqrt(n)) as Time Complexity and O(1) as space complexity

# If we look carefully, all the divisors of a number appear in pairs.
# For example, if n = 100, then the divisor pairs are:
# (1, 100), (2, 50), (4, 25), (5, 20), (10, 10).

# We need to be careful in cases like (10, 10), when both divisors in a pair are equal. In such cases, we should include that divisor only once.

# So Instead of iterating from 1 to n, we only need to iterate from 1 to √n.
# Why? Because for any factor a of n, the corresponding factor b = n / a forms a pair (a, b).
# At least one of the two values in any such pair must lie within the range [1, √n].

# So, we can:

# Iterate from 1 to √n to find all divisors less than or equal to √n.
# For every divisor d of n, add d to the res array. If d is not the square root of n, store its paired divisor n / d in the large array. Since the paired divisors are encountered in descending order, append the elements of large to res in reverse order at the end to obtain all divisors in ascending order.


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
        
import java.util.*;

class GFG {

    public static ArrayList<Integer> getDivisors(int n) {
        
        ArrayList<Integer> divisors = new ArrayList<>();

        // Iterate from 1 to n and check divisibility
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                
                // If 'i' divides 'n' evenly, it's a divisor
                divisors.add(i);
            }
        }

        // Return the list of divisors
        return divisors;
    }   
     
    public static void main(String[] args) {
        int number = 10;

        ArrayList<Integer> divisors = getDivisors(number);

        for (int div : divisors) {
            System.out.print(div + " ");
        }
    }
}

