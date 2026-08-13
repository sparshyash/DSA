import java.util.Scanner;
import java.util.Arrays;
public class Arraystostring 
{
 public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String[] str = new String[4]; // int arr[];//int[] str;
    for(int i =0; i<str.length;i++){
        str[i] = in.next();
    }
    in.close();
    System.out.println(Arrays.toString(str));

 }   
}
