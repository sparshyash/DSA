package Kunal;
public class Xortillotoa {
    public static void main(String[] args) {
        int a=10;
        int p=0;
        for(int i=0;i<=a;i++){
            p=p^i;
        }
        System.out.println(Integer.toBinaryString(p));
    }
}
