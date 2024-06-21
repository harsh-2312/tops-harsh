//q16 .Accept 5 numbers from user and perform sum of array

#include<stdio.h>

int main(){


    int arr[5],i,sum=0;

    printf("enter 5 number:");
    for(i=0;i<5;i++){
        scanf("%d",&arr[i]);
    }

    for(i=0;i<5;i++){

        sum=sum+arr[i];
    }printf("\nsum of number:%d\n", sum);

    return 0;
}