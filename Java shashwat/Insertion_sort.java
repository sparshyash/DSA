public class Insertion_sort{
    public static void main(String[] args){
        // n-1 passes best O(n) worst O(n^2)  space O(1)
        // element ko unsorted array m se uthake sorted array m set krta hai

        int  arr[]=new int[]{5,4,3,1,2};
        int n = arr.length;
        int temp=0;
        for (int i=1;i<n;i++){
            temp=arr[i];
            int j=i-1;
            while(j>=0 && arr[j]>temp){
                arr[j+1]=arr[j];
                j--;
            }
            arr[j+1]=temp;
        }
        for(int a=0;a<n;a++){
            System.out.println(arr[a]);
        }
        
        }
}