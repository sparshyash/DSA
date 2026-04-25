class Twosum {
    public int[] twoSum(int[] nums, int target) {
        int n= nums.length;
        HashMap<Integer,Integer> map=new HashMap<>();
        int complement=0;

        for(int  i =0;i<n;i++){
            complement =target-nums[i];
            if (map.containsKey(complement)){
                return new int []{map.get(complement),i};
            }
            map.put(nums[i],i);

        }
        return new int[]{-1,-1};
    }
}
// O(n)

// 2nd approach 
