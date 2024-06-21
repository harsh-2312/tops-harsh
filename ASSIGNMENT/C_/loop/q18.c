//q18.c
//Write a C Program to Print the Multiplication Table of N


#include<stdio.h>

int main(){

    int i, n;
    printf("enter a num:");
    scanf("%d", &n);

    for(i=1;i<=10;i++){
        printf("%d * %d = %d\n",n ,i,n * i);
    }


    return 0;
}