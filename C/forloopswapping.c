#include <stdio.h>
int main(){
    int arr[] ={5,4,3,2,1};
    int n= sizeof(arr)/sizeof(arr[0]);
    for(int i=0;i<(n-1)/2;i++){
        int temp=arr[i];
        arr[i]=arr[n-1-i];
        arr[n-1-i]=temp;

    }
}