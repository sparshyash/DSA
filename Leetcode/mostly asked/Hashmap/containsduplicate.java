import java.util.HashMap;

class containsDuplicate {
    public static void main(String[] args) {
        int arr[]={1,2,3,4,1};
        boolean ans = containsduplicate(arr);
        System.out.println(ans);
    }
    public static boolean containsduplicate(int arr[]){
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            if (hashmap.containsKey(arr[i])) {
                return true;
            }
            hashmap.put(arr[i], i);
        }
        return false;
    }
}