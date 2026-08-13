import java.util.HashMap ;

class twosum2 {
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer , Integer > map= new HashMap<>();
        for(int i = 0;i<numbers.length ;i++){
            int complement = target-numbers[i];
            if(map.containsKey(complement)){
                return new int[]{ map.get(complement)+1,i+1};
            }
            map.put(numbers[i],i);
        }
        return new int[]{-1,-1};
    }

    public static void main(String[] args) {
        int[] numbers = {2, 7, 11, 15};
        int target = 9;
        twosum2 solution = new twosum2();
        int[] result = solution.twoSum(numbers, target);
        System.out.println("Indices: [" + result[0] + ", " + result[1] + "]");
    }
} 
