public class Linear_Search {
    public static void main(String[] args) {
        System.out.println("Hello!");
        //search in range
         int[] arr = {4,8,5,6,3,5};
        /* int target = 50;
        System.out.println(linearSearch(arr,target,2,5));*/
        System.out.println(min(arr));
    
        

    }
    // assume arr.length isn't = 0
    static int min(int[] arr){
        int ans = arr[0];
        for(int i =1;i<arr.length;i++){
            if(arr[i]<ans){
                ans = arr[i];
            }
        }
        return ans;
    }/*
    static int linearSearch(int[] arr, int target,int start,int end){
        if (arr.length==0) 
        {
            return -1;    
        }
        // run a for loop
        for(int index = start;index<=end;index++){
            // check for element at every index if it is target or not
            int element = arr[index];
            if(element==target){
                return index;
            }
            
        }
        return -1;*/
        // find min no.

    }
    

