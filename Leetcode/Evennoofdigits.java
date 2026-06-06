// LEETCODE 1295

public class Evennoofdigits {
    public static void main(String[] args) {
        int[] nums ={12,345,2,6,7896};
       
                   System.out.println(Findnumbers(nums));
                    System.out.println(digits2(456));
                
            }
            static int Findnumbers(int[] arr){
                int count =0;
                for(int num:arr) {
                    if(even(num)){
                        count++;
                    }
                    
                }
                return count;
            }
            // function to check whether no. contains even no. of digits
            static boolean even(int nums){
                int numberofdigits=digits(nums);
                /* if(numberofdigits % 2==0){
                 return true;
                }
                return false;//return numberofdits %2==0;
                */
                return numberofdigits%2==0;
         
             }
            static int digits2(int num){
                if(num<0){
                    num=num*(-1);
                }
                return (int)(Math.log10(num))+1;
            }
            
          
            
            
            
             static int digits(int  nums){
                int count=0;
                if(nums<0){
                    nums = nums*(-1);
                }
                    if(nums==0){
                    return 1;
                    }
                while (nums>0) {
                    
                
                    count++;
                    nums=nums/10;
                }
                return count;
                
            
        
        
    }
        

}