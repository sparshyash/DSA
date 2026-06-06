// leetcode1672
public class RichestComputerWealth {
    public static void main(String[] args) {
      int[][] accounts = {{1,2,3},{3,2,1}};
      System.out.println(maximumWealth(accounts));
        
    }
    public static int maximumWealth(int[][] accounts) {
        int max=0;
        
        for(int person=0;person<accounts.length;person++){
            //WHEN you start a new column take addition of all previous  
            int sum=0;
            for(int account=0;account<accounts[person].length;account++){// person=row
                //account=col
                
                
                sum += accounts[person][account];
            }
                if(sum>max){
                    max=sum;
                }
                 

            }
        return max;


        
    }
}
