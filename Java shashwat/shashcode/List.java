package Collection_framework;


import java.util.*;
import java.util.ArrayList;
import java.util.Comparator;

public class List {
        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(8);
        

        System.out.println(list);
        System.out.println(list.size());
        list.remove(Integer.valueOf(3));
        System.out.println(list);
        list.remove(1);
        System.out.println(list);
        System.out.println(list.get(0));
        System.out.println(list.contains(8));
        System.out.println(list.set(1, 7));


        list.sort(new Comparator<Integer>() {
            public int compare(Integer A, Integer B) {
                return B - A; // Descending order
            }
        });

        System.out.println(list);

        

        List<Student> list1 = new ArrayList<>();
        list1.add(new Student(8, "GS"));
        list1.add(new Student(1, "S"));
        list1.add(new Student(2, "SG"));
        list1.add(new Student(8, "MK"));

        list1.sort(new Comparator<Student>() {
            public int compare(Student A, Student B) {
                int res= B.roll_no - A.roll_no;
                if (res==0){
                    return A.name.compareTo(B.name);
                }
                
            }
        });

        System.out.println(list1);
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
