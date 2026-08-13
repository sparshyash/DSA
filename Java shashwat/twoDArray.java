import java.util.Scanner;
import java.util.Arrays;
public class twoDArray {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        /*
        1 2 3
        4 5 6
        7 8 9 
        */ 
        // Syntax : int[][] arr = new int[3][];
        // System.out.println(arr.length); print no. of rows always
        // it is not mandatory to add column no.s but you have to mention row no.s
        /* int[][] arr2D = {
            {1,2,3},// 0th index
            {4,5},// 1stindex
            {7,8,9,10}// 2nd index
        };*/
        //input a 2d array
        int[][] arr = new int[3][3];
        for(int row =0;row<arr.length;row++){
            for(int col =0; col < arr[row].length;col++){
                arr[row][col] = in.nextInt();

            }
        }
            for(int row =0;row<arr.length;row++){
                for(int col =0; col < arr[row].length;col++){
                    System.out.print(arr[row][col] + " ");
        }
        System.out.println();
    }
    for(int row = 0; row<arr.length;row++){
        System.out.println(Arrays.toString(arr[row]));
    }
    for(int[] a: arr){
        System.out.println((Arrays.toString(a)));
    }
    in.close();
    }
    
}
