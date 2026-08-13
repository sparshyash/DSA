

class OOPS1Theory {
    public static void main(String[] args) {
        

        Student  Sparsh= new Student();
        System.out.println(Sparsh);
        Sparsh.rollno=15;
        Sparsh.marks=99.9f;
        System.out.println(Sparsh.marks);
        System.out.println(Sparsh.rollno);
        Sparsh.greeting();

    }

   
}
    
class Student {
     int rollno;
     float marks=80f;
     String name;
    void greeting(){
        System.out.println("Hello Mr."+ name);
    }
     
 
 Student() {
     this.rollno=15;
     this.marks=12.6f;
     this.name="Sparsh";
 }
}    
     
