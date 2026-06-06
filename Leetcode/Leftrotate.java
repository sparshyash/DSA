import java.util.ArrayList;
import java.util.Arrays;


public class Leftrotate {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        System.out.println(Arrays.toString(Rotate(arr, 2)));
    }
    public static int[] Rotate(int[] nums,int k){
        k=k%nums.length;
        ArrayList<Integer> num=new ArrayList<>();
        ArrayList<Integer> num2=new ArrayList<>();
        for(int i=nums.length-k;i<nums.length;i++){
            num.add(nums[i]);

        }
        for(int i=0;i<=k;i++){
            num2.add(nums[i]);
        }
        for(int i=0;i<k;i++){
            nums[i]=num.get(i);
        }
        for(int i=k;i<nums.length;i++){
            nums[i]=num2.get(i-k);
        }
        return nums;

    }
}
