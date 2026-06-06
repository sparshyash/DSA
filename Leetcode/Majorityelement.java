class majorityElement {
    public static void main(String[] args) {
        int[] nums={2,2,1};
        System.out.println(majorityElement(nums));
        
    }
    static int majorityElement(int[] nums) {
        
        
        for( int i=0;i<nums.length;i++){
            int num=i;
            int count=0;
            if(nums[i]==num){
                count++;
            }
            if(count>(nums.length/2)){
                return nums[i];
            }
           
        }
        return -1;
        
        
    }
}