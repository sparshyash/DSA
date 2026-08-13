public class pattern {
    public static void main(String[] args) {
        int n=5;
        int nsp=4;
        int nst=1;
        // for(int i=n;i>=1;i--){
            // for(int j=0;j<=3;j++){
            //     System.out.print(j);
            // }
            // for(int j=0;j<=i;j++){
            //     System.out.print(j);
            //
            // for(int j=0;j<=i;j++){
            //    System.out.print(i);
            // }
            
            // for(j=1;j<=i;j++){
            //     System.out.print(j);
            // }
            
            
            // System.out.print("\n");
            // PYRAMID
        // for(int i=1;i<=5;i++){
        //     for(int k=0;k<nsp;k++){
        //         System.out.print(" ");
        //     }
        //     for(int j=1;j<=2*i-1;j++){
        //         System.out.print("*");
        //     }
        //     nsp--;
        //     nst++;
        //     System.out.println();
        // }
        // ULTA PYRAMID
        // for(int i=5;i>=1;i--){
        //     for(int k=n-i;k>=1;k--){
        //         System.out.print(" ");
        //     }
        //     for(int j=2*i-1;j>=1;j--){
        //         System.out.print("*");
        //     }
            
            
        //     System.out.println();
        // }
        // for(int i=5;i>=1;i--){
        //     for(int k=n-i;k>=1;k--){
        //         System.out.print(" ");
        //     }
        //     for(int j=2*n-1;j>=1;j--){
        //         System.out.print("*");
        //     }
            
            
     //System.out.println();
// }
 for(int i=1;i<=2*n-1;i++){
           if(i>n){
               for(int k=2*n-i;k>=1;k--){
                    System.out.print("*");
               }
               System.out.println();
               continue;
            
            }
        for(int j=i;j>=1;j--){

               System.out.print("*");
        }
            
            
        System.out.println();
    }
    //     for(int i=1;i<=n;i++){
    //         for (int j=1;j<=i;j++){
    //             if((i+j)%2==0){
    //                 System.out.print("1");
    //             }
    //             else{
    //                 System.out.print("0");
    //             }
    //         }
            
            
    //         System.out.println();
    //     }
    // for(int i=1;i<=n;i++){
    //     for (int j=1;j<=i;j++){
    //         System.out.print(j);
    //     }
    //     for(int l=2*(n-i);l>=1;l--){
    //         System.out.print(" ");
    //     }
    //     for(int k=i;k>=1;k--){
    //         System.out.print(k);
    //     }
        
        
    //     System.out.println();
    //     }
    // int space=1;
    // for(int i=1;i<=n;i++){
    //     for (int j=1;j<=i;j++){
    //         System.out.print(space+" ");
    //         space++;
    //     }

        
        
    //     System.out.println();
    //     }

    // for(int i=n;i>=1;i--){
    //     for(int j=0;j<i;j++){
    //         System.out.print((char)(65+j));
    //     }
    //     System.out.println();
    // }

    // }
    // for(int i=1;i<=n;i++){
    //     for(int j=n-i;j>=1;j--){
    //         System.out.print(" ");
    //     }
    //     for(int l=0;l<i;l++){
    //         System.out.print((char)(65+l));
    //     }
    //     for(int k=i-2;k>=0;k--){
    //         System.out.print((char)(65+k));
    //     }
    //     System.out.println();
    // }
    // for(int i=1;i<=n;i++){

    //     for(int j=n-i;j<n;j++){
    //         System.out.print((char)(65+j));
    //     }

    //     System.out.println();
    // }
    // for(int i=1;i<=n;i++){

    //     for(int j=n-i;j<n;j++){
    //         System.out.print((char)(65+j));
    //     }

    //     System.out.println();
    // }
    for(int i=n;i>=1;i--){
        for (int j=1;j<=i;j++){
            System.out.print("*");
        }
        for(int l=2*(n-i);l>=1;l--){
            System.out.print(" ");
        }
        for(int k=i;k>=1;k--){
            System.out.print("*");
      }
      System.out.println();
    }

     for(int i=1;i<=n;i++){
         for (int j=1;j<=i;j++){
             System.out.print("*");
         }
         for(int l=2*(n-i);l>=1;l--){
             System.out.print(" ");
         }
         for(int k=i;k>=1;k--){
             System.out.print("*");
       }
       System.out.println();
    }
    for(int i=1;i<=n-1;i++){
        int stars=i;

     for(int j=1;j<=stars;j++){

            System.out.print("*");
     }
     for(int k=2*(n-i);k>=1;k--){
        System.out.print(" ");
     }
     for(int h=1;h<=stars;h++){
        System.out.print("*");
     }
         
         
     System.out.println();
 }
 for(int i=1;i<=2*n;i++){
    System.out.print("*");
 }
 System.out.println();
for(int i=n-1;i>=1;i--){
    int stars=i;

 for(int j=1;j<=stars;j++){

        System.out.print("*");
 }
 for(int k=2*(n-i);k>=1;k--){
    System.out.print(" ");
 }
 for(int h=1;h<=stars;h++){
    System.out.print("*");
 }
     
     
 System.out.println();
}
    }
}