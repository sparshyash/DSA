//pointers store addess of variable , array ,structure and other pointer also denoted by'*' known as DEREFERNCY OPERATOR 
#include<stdio.h>
#include<math.h>
int main(){
    int a=10;
    int *ptr;// pointer declaration. Integer type ki value ke liye integer type ka pointer 
    int **pp;// double pointer
    pp=&ptr;
    ptr=&a;//& denoted address of // pointer initialization
    printf("%x",ptr);// print value stored in ptr i.e., adrees of 'a' . GENERALLY ADDRESS IN HEXADECIMAL 
    printf("%p",ptr);// print value stored in ptr i.e., adrees of "a"
    printf("%x",pp);// print address of ptr
    printf("%d",*ptr); // print value stored at the address which is stored in the ptr 
    printf("%d",**pp);
    printf("\n"); 
    printf("%d",sizeof(int));
    printf("\n");
    printf("%d",sizeof(float));
    sizeof(char);
    int gh[10];
    int *hh;
    hh=&gh[0];//or you can write hh = gh
    for (int i = 0; i < 10; i++){
        printf("%d ",*(hh+i));// print elements of array
        int sum = sum+*(hh+i);// add array elements
    }
    
    

    return 0;

}