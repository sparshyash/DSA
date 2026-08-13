import java.util.Scanner;
import java.util.ArrayList;

public class Arraylist {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Hello!");
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        // initialisation
        for(int i =0;i<3;i++){
            list.add(new ArrayList<>());
        }
        // addition 
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                list.get(i).add(in.nextInt());
            }
        }
        System.out.println(list);
        /*
         syntax
         Arraylist<datatype> var_name = new Arraylist<your choice to add or not add datatype here>();
         */
        /*ArrayList<Integer> list = new ArrayList<>();
        list.add(123);
        list.add(456);
        System.out.println(list);
        System.out.println(list.contains(123));
        System.out.println(list.set(0, 100));// change value at 0 index to 100
        */
        in.close();
    }
}
