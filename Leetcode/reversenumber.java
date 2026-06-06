

public class reversenumber {
    public static void main(String[] args) {
        int n=531;
        System.out.println(Reverse(n));
    }
    public static int Reverse(int n){
        int sum=0;
        if(n==0||n==1){
            return n;
        }
        else{
            while (n>0) {
                sum=sum*10+n%10;
                n=n/10;
            }
        }
        return sum;
    }
}
