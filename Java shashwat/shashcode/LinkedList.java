import java.util.*;

public class LinkedList {
    public static void main(String[] args) {








        // Linked List 
        List<Integer> list2 = new LinkedList<>();
        list2.add(1);
        list2.add(2);
        list2.add(3);
        list2.add(8);
        

        System.out.println(list2);
        System.out.println(list2.size());
        list2.remove(Integer.valueOf(3));
        System.out.println(list2);
        list2.remove(1);
        System.out.println(list2);
        System.out.println(list2.get(3));
        System.out.println(list2.contains(8));
        System.out.println(list2.set(1, 7));

        
        list2.sort(new Comparator<Integer>() {
            public int compare(Integer A, Integer B) {
                return B - A; // Descending order
            }
        });
}
}

class Student {
    int roll_no;
    String name;

    public Student(int roll, String name) {
        this.roll_no = roll;
        this.name = name;
    }

    public String toString() {
        return name + " (" + roll_no + ")";
    }
}
