public class OOPS6 {
     class Readonly{
        private int age;
        private String name;
     }
     
     Readonly(){
      this.age=22;
      this.name="SPARSH";

     }
     public int getage(){
      return this.age;
     }
     public String getname(){
      return this.name;
     }
     class WriteOnly{
      private int age;
      private String  name;

     }
     public void setAge(int age){
      this.age=age;
     }
     public void setName(String name){
      this.name=name;
     }
     class ReadWrite{
      private int age;
      private String name;

     }
     ReadWrite(){
      this.age=1;
      this.name="Sparsh";
     }

}
