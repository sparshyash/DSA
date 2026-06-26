class maximumproductsubarray {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int max = nums[0]; 
        int prefix = 1, suffix = 1;

        for (int i = 0; i < n; i++) {
            if (prefix == 0) prefix = 1;
            if (suffix == 0) suffix = 1;

            prefix *= nums[i];
            suffix *= nums[n - 1 - i];

            max = Math.max(max, Math.max(prefix, suffix));
        }

        return max;
    }
    public static void main(String[] args) {
        maximumproductsubarray obj = new maximumproductsubarray();
        int arr[] = {2, 3, -2, 4};
        System.out.println(obj.maxProduct(arr));
    }
}