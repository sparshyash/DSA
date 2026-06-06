import java.util.Arrays;

public class Searchin2DArrays {
    public static void main(String[] args) {
        System.out.println("Hello!");
        int[][] arr = {
            {1,2,3},{4,5,6,7},{8,9},{18,12}
        };// or new int[][]{.....}
        int target = 18;
        int[] ans = Search(arr,target);// format of rturn is {row,col}.
        System.out.println(Arrays.toString(ans));
        System.out.println("the minm alue in array is" +max(arr));
        System.out.println(Integer.MIN_VALUE);
    }

    
    static int[] Search(int[][] array, int target){
        for(int row =1;row<array.length;row++){
            for(int col=1;col<array[row].length;col++){
                if(array[row][col]==target){
                    return new int[]{row,col};
                }
            }
        }
    
    return new int[]{-1,-1};
} 
    static int max(int[][] arr){
        int max = Integer.MAX_VALUE;
        for(int[] ints: arr){
            for(int anInt: ints){
                if(anInt<max){
                        max = anInt;
                        System.out.println(max);
                    }

                }
            }return max;

        }
    
}
