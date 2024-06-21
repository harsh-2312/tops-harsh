//q4
//WAP to find factorial using recursion

#include<stdio.h>

int factorial(int n);

int main(){

    int n;
    printf("enter number:");
    scanf("%d", &n);

    printf("factorial is:%d\n", factorial(n));

    return 0;
}

int factorial(int n){
    if(n==0){
        return 1;
    }
    int fact = factorial(n-1);
    fact= fact * n;
    return fact;
}