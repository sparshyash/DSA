#include<stdio.h>
struct  employee {
    int code;
    char name[50];
    float salary;
};
void display(struct employee *aa){
    printf("\n code = %d",aa->code);
}

int main(){
    struct employee aa;
    printf("Enter Code");
    scanf("%d",& aa.code);
    display(&aa);
   
}