//q25
//.Accept 5 expense from user and find average of expense
#include<stdio.h>

int main(){

    int ex1,ex2,ex3,ex4,ex5, average,total;

    printf("enter expense:");
    scanf("%d", &ex1);

    printf("enter expense:");
    scanf("%d", &ex2);

    printf("enter expense:");
    scanf("%d", &ex3);

    printf("enter expense:");
    scanf("%d", &ex4);

    printf("enter expense:");
    scanf("%d", &ex5);

    total=ex1+ex2+ex3+ex4+ex5;
    
    average=total/5;

    printf("average of expense:%d\n", average);

    return 0;

    


}