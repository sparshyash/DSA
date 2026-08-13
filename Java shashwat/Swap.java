

public class Swap {
    public static void main(String[] args) {
        int a =10;
        int b=20;
        String name= "Sparsh";
        greet(name);
        System.out.println(name);
        // swapping of both
        int temp = a;
        a=b;
        b=temp;
        System.out.println(a+" "+b);
        swap(a, b);
        System.out.println(a+" "+ b);
    }
    static String greet(String naam){
        naam = "Yash ";
        return naam;
    }
    static void swap(int a, int b){
        int temp=a;
        a=b;
        b=temp;
        return;
    }
}
