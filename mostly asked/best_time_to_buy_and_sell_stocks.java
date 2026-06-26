class best_time_to_buy_and_sell_stocks {
    public static int maxprofit(int[] arr){
        int n =arr.length;
        int profit=0;
        int min=Integer.MAX_VALUE;

        for(int i=0;i<n;i++){
            min=Math.min(min,arr[i]);
            profit=Math.max(profit,arr[i]-min);
        }
        return profit;
        
    }
    public static void main(String[] args) {
        int arr[]={7,1,5,3,6,4};
        System.out.println(maxprofit(arr));
    }
}