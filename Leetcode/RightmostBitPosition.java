public class RightmostBitPosition {
    public static void main(String[] args) {
        int n = 8; // Binary: 10010
        int position = 1; // Bit positions start from 1

        while ((n & 1) == 0) { // Check if LSB is 0
            n = n >> 1; // Right shift
            position++; // Move to the next bit
        }

        System.out.println("Rightmost Set Bit Position: " + position);
    }
}
