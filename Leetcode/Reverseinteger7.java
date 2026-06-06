public class Reverseinteger7 {
    public static int reverse(int x) {
        long sum=0;
        int rem=0;
        while(x!=0){
            rem=x%10;
            sum = sum*10+rem;
            x/=10;
        }
        if (sum > Integer.MAX_VALUE || sum < Integer.MIN_VALUE) {
            return 0;  // 32 bit ka matlab 2,147,483,647 and -2,147,483,648 k under
        }
        
        return (int) sum;
    }
    public static void main(String args[]) {
        int x = 123;
        int ans = reverse(x);
        System.out.println(ans);
    }
}
