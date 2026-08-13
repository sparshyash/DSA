public class RightmostBit {
    public static void main(String[] args) {
        int n = 8;
        
        int position = (int) (Math.log(n & -n) / Math.log(2)) + 1;
        
        System.out.println("Rightmost Set Bit Position: " + position);

    }
}
