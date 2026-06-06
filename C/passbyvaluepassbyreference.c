#include<stdio.h>
/* void swap(int a,int b){//PASS BY VALUE ; In c if you made function above main you don't need to declare it 
    int temp=a;
    a=b;
    b=temp;
    printf("%d %d",a,b);// function calling  me arguments or initialization or declaration me parametes

}
int main(){
    int a=10,b=20;//in pass by value a copy of value is created and no change in original value.
    swap(a,b);
    printf("\n");
    printf("%d %d",a,b);
}*/
void swap(int *x,int *y){// PASS BY REFERNCE 
    int temp= *x;
    *x=*y;
    *y=temp;
    printf("%d %d",*x,*y);
    return;
}
int main(){
    int a=10,b=20;
    swap(&a,&b);
    printf("%d %d",a,b);
    return 0;
}