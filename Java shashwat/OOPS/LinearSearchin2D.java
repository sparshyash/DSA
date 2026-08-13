package Shashcode;

public class LinearSearchin2D {
    public static void main(String[] args) {
        int[][] arr = {
            {1,2,3},
            {4,5,6}
        };
        int target=5;
        LinearSearch(arr ,target,false);
    }
    public static void LinearSearch(int arr[][],int target,boolean findlast){
        boolean found=false; 
        int outerindex=-1;
        int innerindex=-1;
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr[i].length;j++){
                if(target == arr[i][j]){
                   outerindex=i;
                   innerindex=j;
                   if(findlast==false){
                    found=true;
                    break;
                   } 
                }

                } 
                if (found==true) {
                    break;
            }
            if(outerindex==-1){
                System.out.println("Fails");

            }
            else{
                System.out.println("Found at :"+ outerindex);
            }
        }
    }
    
}