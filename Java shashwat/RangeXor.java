
public class RangeXor {
    public static void main(String[] args) {
        int a=10;
        int b=3;
        int ans=Xor(a)^Xor(b-1);
        System.out.println(Xor(a));
        System.out.println(ans);
    }
    public static int Xor(int n){
        if (n%4==0) {
            return n;
        }
        else if (n%4==1) {
            return 1;
        }
        else if (n%4==2) {
            return n+1;
        }
        return 0;
    }
}