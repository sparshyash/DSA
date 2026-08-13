#include<stdio.h>
// self refernial structure -- structure which contains pointer to itself matlab same data type ki structure is called self refernial structure
struct student
{
    int roll;
    char name[20];
    float marks;
};

int main()
{
    struct student aa,*ptr;
    ptr=&aa; // ptr is pointer to structure student
    printf("Enter roll number: ");
    scanf("%d",&ptr->roll);
    printf("Enter name: ");
    scanf("%s",ptr.name);
    printf("Enter marks: ");
    scanf("%f",&ptr->marks);
    printf("Roll number: %d\n",ptr->roll);
    printf("Name: %s\n",ptr->name);
    printf("Marks: %f\n",ptr->marks);

}