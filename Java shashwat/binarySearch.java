package BINARYSAERCH;

public class BinarySearch {
    public static void main(String[] args) {
       int[] name={4,5,6,7,8,9,10,11,12,13,14};
       binarySeacrh(name, 10); 
        
    }
    static void binarySeacrh(int[] arr,int target){
        int start=0;
        int end = arr.length-1;
       
        while (start<=end){
            // find th middle element
            int mid=start+(end-start)/2;
            if(mid>target){
                end=mid-1;
            }
            else if(mid<target){
                start=mid+1;
            }
            else{
                System.out.println(mid);
            }
            
        } 
        System.out.println("No");
            
        }

    }


