public class theft {
    public static String read(int n, int []book, int target){
        // Write your code here.
        for(int i=0;i<n-1;i++){
            int cam=i;
            if(book[cam]+book[i+1]==target){
                return "YES";
            }
        }
        return "NO";
    }
    public static void main(String[] args) {
        int[] book = {198, 136, 330, 455, 709, 547, 203, 882, 464, 726, 339, 347, 985, 955, 771, 
            598, 131, 181, 56, 350, 504, 761, 554, 514, 431, 853, 424, 360, 75, 765, 135, 
            204, 957, 461, 171};
int target = 1092;
int n = book.length;

String result = theft.read(n, book, target);
System.out.println(result);
    }
}