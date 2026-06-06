#include<stdio.h>
int main(){
    int nsp=4;
    int nst=1;

    for(int i=1;i<=5;i++){
        for (int j = 1; j <=nsp; j++)
        {
            /* code */
            printf(" ");

        }
        
        for (int j=1;j<=nst;j++){
            printf("%d",j);

        }
        for (int j= i -1 ; j>=1; j--)
        {
            printf("%d",j);
        }
        
        nsp--;
        nst+=1;
        printf("\n");
            /* code */
        
        
    }return 0;
}