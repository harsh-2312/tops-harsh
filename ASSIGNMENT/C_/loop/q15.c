//q15
//Calculate sum of 10 numbers using of while loop

#include<stdio.h>

int main(){

    int i, num, sum=0;

    printf("enter 10 number\n");

    i=1;
    while(i<=10){
        printf("number %d=",i);
        scanf("%d",&num);
        i++;
        sum= sum + num;
    }printf("sum of 10 number:%d\n", sum);


    return 0;
}