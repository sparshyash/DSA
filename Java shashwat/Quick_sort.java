public class Quick_sort{
    public static void main(String[] args){
        // best O(nlogn) worst O(n^2) space O(logn)
        // pivot element choose krta hai or uske left m chote element or right m bade element set krta hai or phir recursively sort krta hai left or right subarray ko

        int  arr[]=new int[]{5,4,3,1,2};
        int n = arr.length;
        quickSort(arr,0,n-1);
        for(int a=0;a<n;a++){
            System.out.println(arr[a]);
        }
        
        }
    public static void quickSort(int[] arr,int low,int high){
        if(low<high){
            int pi=partition(arr,low,high);
            quickSort(arr,low,pi-1);
            quickSort(arr,pi+1,high);
        }
    }
    public static int partition(int[] arr,int low,int high){
        int pivot=arr[high];
        int i=low-1;
        for(int j=low;j<high;j++){
            if(arr[j]<pivot){
                i++;
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
        int temp=arr[i+1];
        arr[i+1]=arr[high];
        arr[high]=temp;
        return i+1;
    }
}