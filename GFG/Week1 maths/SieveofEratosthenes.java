import java.util.ArrayList;
import java.util.List;

public class SieveofEratosthenes {
    // Check if a number is prime
    public static boolean isPrime(int num) {
        if (num < 2)
            return false;

        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0)
                return false;
        }

        return true;
    }
    
    public static ArrayList<Integer> sieve(int n) {
        ArrayList<Integer> res = new ArrayList<>();

        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) {
                res.add(i);
            }
        }

        return res;
    }

    public static void main(String[] args) {
        int n = 35;

        List<Integer> res = sieve(n);

        for (int ele : res) {
            System.out.print(ele + " ");
        }
    }
}