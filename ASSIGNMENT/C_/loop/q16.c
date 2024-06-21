//q16
//Calculate the Sum of Natural Numbers Using the While Loop

#include<stdio.h>
int main(){

    int i, num=0, sum=0;

    printf("enter number:");
    scanf("%d",&num);

    i=0;
    while(i<=num){
    sum= sum + i;
    ++i;

    }printf("sum is=%d\n",sum);



    return 0;
}