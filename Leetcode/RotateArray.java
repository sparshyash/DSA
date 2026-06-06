import java.util.Arrays;

public class RotateArray {
    public static void main(String[] args) {
        int[] arr={1,2,3,4,5};
        System.out.println(Arrays.toString(rotate(arr, 2)));
    }
    
        public static int[] rotate(int[] nums, int k) {
            int l=0;
            int h=nums.length-1;
            while(l<h){
                int temp=nums[l];
                nums[l]=nums[h];
                nums[h]=temp;
                l++;
                h--;
            }
            l=0;
            h=k-1;
            while(l<h){
                int temp=nums[l];
                nums[l]=nums[h];
                nums[h]=temp;
                l++;
                h--;
            }
            l=k;h=nums.length-1;
            while(l<h){
                int temp=nums[l];
                nums[l]=nums[h];
                nums[h]=temp;
                l++;
                h--;
            }
            
            return nums;
        }
    }

