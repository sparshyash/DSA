// Also known as Exit controlled loop 

public class do_while{
    
    public static void main(String[] args) {
        int a = 1;

        do {

            System.out.println(a);
            a++;
        }while(a==0);// runs at least one time even if condition is false
        System.out.println("Ok");
    }
}