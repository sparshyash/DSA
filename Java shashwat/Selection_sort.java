public class Selection_sort{
    public static void main(String[] args){
        // n-1 passes best O(n^2) worst O(n^2)  space O(1)
        //  in element dhundke use swap krta hai or end m le aata hai first element ko of unsorted array 
        
        int  arr[]=new int[]{5,4,3,1,2};
        int n = arr.length;
        int temp=0;
        for (int i=0;i<n-1;i++){
            int min_index=i;
            for(int j=i+1;j<n;j++){
                    if(arr[j]<arr[min_index]){
                        min_index=j;
                    }
            }
            temp=arr[i];
            arr[i]=arr[min_index];
            arr[min_index]=temp;
        }
        for(int a=0;a<n;a++){
            System.out.println(arr[a]);
        }
        
        }
}