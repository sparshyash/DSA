import java.util.HashMap;

class containsduplicate2 {
    public static void main(String[] args) {
        int arr[]= {1,2,3,1} ;
        boolean ans = containsduplicate(arr, 3) ;
        System.out.println(ans) ;
    }
    public static boolean containsduplicate(int[] nums, int k) {
        int n = nums.length ;

        HashMap<Integer , Integer> map=new HashMap<>();
        for (int i=0;i<nums.length;i++){
            if (map.containsKey(nums[i])){
                int j = map.get(nums[i]) ;
                if(i-j <=k){
                    return true;
                }
            }
            map.put(nums[i],i) ;
        }
        return false;
    }
}