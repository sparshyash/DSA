package Recurssion;

public class TowerOfHanoi {
    public static void main(String[] args) {
        int n=5;
        System.out.println(Hanoi(n, null, null, null););

    }
    public static void Hanoi(int n,String src,String helper,String dest){
        if(n==1){
            System.out.println("transfer"+n+"from"+src+"to"+dest);
            return;
        }
        Hanoi(n-1, src, helper, dest);

    }
    
}