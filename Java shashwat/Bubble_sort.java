public class Bubble_sort{
    public static void main(String[] args){
        // n-1 passes best O(1) worst O(n^2)  space O(1)

        int  arr[]=new int[]{5,4,3,1,2};
        int n = arr.length;
        int temp=0;
        int flag=0;
        for (int i=0;i<n-1;i++){
            for(int j=0;j<n-1-i;j++){ // ar ek sort m ek element last m set hojayega to use check meat kro next pass me 
                    if(arr[j]>arr[j+1]){
                        temp=arr[j];
                        arr[j]=arr[j+1];
                        arr[j+1]=temp;
                        flag=1;
                    }
                    if(flag==0){
                        
                        break;
                    }
                    else{
                        flag=0;
                    }

                    }
        }
        for(int a=0;a<n;a++){
            System.out.println(arr[a]);
        }
        
        }
      

        
    }
// swapping krta hai aaju baju balo ki or krte krte end m le aata hai last element ko