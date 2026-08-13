public class Bitsset {
    public static void main(String[] args) {
        int n=45;
        System.out.println(Integer.toBinaryString(n));
        System.out.println(Setbits(n));
    }
    public static int Setbits(int n){
        int count =0;
        // while (n > 0) {
        //     count++;
        //     n-=(n & -n);

        // }
        // return count;
        while(n>0){
            count++;
            n=n&(n-1);
        }
        return count;
    }
    
}
