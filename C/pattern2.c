#include<stdio.h>
int main(){
    int nst =5;
    int nsp=1;
    for(int i=1;i<=9;i++){
        printf("*");
    }for(int i=1;i<=5;i++){
        for (int j= 1 ; j <=nst; j++)
        {
            /* code */
            printf("* ");

        }
    
        for (int k=1;k<=nsp; k++)
        {
                /* code */
                printf(" ");
        }
        
        nsp++;
        nst--;
        printf("\n");
    }
        
        
    return 0;
}