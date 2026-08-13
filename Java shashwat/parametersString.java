

import java.util.Scanner;

public class parametersString {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("enter name");
        String name = in.next();
        String personalised = greet(name);
        System.out.println(personalised);
        in.close();
    }
    static String greet(String name){
        String message = "Hello" +"  " + name;
        return message;
    }
}
