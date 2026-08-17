package GFG.week2;

public class moorevoting {
    public static void main(String[] args) {
        int arr[]={1,2,1,3,4,5,1,6};
        System.out.println(majorityelement(arr));
    }

    static int majorityelement(int[] arr){
        int count=0;
        int candidate=-1;

        for(int num:arr){
            if(count==0){
                candidate=num;
            }
            count+= (num==candidate)?1:-1; // Ternany operator
        }

        return candidate;
    }
}
