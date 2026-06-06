#include<stdio.h>
int main(){// CAN BE APPLIED TO AN UNSORTED ARAY ALSO
    int arr[5],search,i;// LINEAR SEARCH HAS TIME COMPLEXITY OF O(n) AND SPACE COMPLEXITY O(1)
    printf("Enter the elements in a sorted manner");
    for(int i=0;i<4;i++){
        scanf("%d",&arr[i]);
    }
    printf("\nEnter target");
    scanf("%d", &search);
    for(int i=0;i<4;i++){
        if(search==arr[i])
        printf("\n position is %d ",i+1);
    }
    return 0;
}