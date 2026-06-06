#include<stdio.h>
int main(){
    int min=0;
    for(int i=1;i<=9;i++){
        for(int j=1;j<=9;j++){
            int a=i;
            if(i>5)
            a=10-i;
            int b=j;
            if(j>5)
            b=10-j;
            if(a>b){
                min=b;
                printf("%d",9-min);
            }
            else{
                min=a;
                printf("%d",9-min);
            }
        }
        printf("\n");
    }return 0;
}