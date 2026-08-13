public class Mathsfordsa{
     public static void  main(String[] args) {
//         int [] arr = {1,2,3,4,3,2,1};
//         System.out.println(ans(arr));
//     }
//     public static int ans(int[] a){
//         int unique =0;
//         for(int n : a){
//             unique^=n;
//         }
//         return unique;
          //  int n=6;

          //  int ans=0;
          //  int base =5;
          //  while(n>0){
          //      int last =n & 1;
          //      n=n>>1;
          //      ans+=last*base;
          //      base=base*5;
          //  }
          //  System.out.println(ans);
          int n = 50;
          int base = 10;
          int ans=(int)(Math.log(n)/Math.log(base)) +1; 
          System.out.println(ans);
     
           
               
                   for (int i = 0; i < 5; i++) {
                       // Calculate sum using 2^n formula
                       int rowSum = (int) Math.pow(2, i);
                       System.out.println("Sum of row " + i+1 + " = " + rowSum);
                       System.out.println(1<<4);
                   }
               
           
           
     }
       
}