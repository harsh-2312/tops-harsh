//q6
//WAP to print Fibonacci series up to given numbers
#include<stdio.h>

int main(){

    int i, n , a = 0 ,b = 1,nextnum = a + b;
    printf("enter num:");
    scanf("%d", &n);
    printf("%d  %d ", a , b);

    for(i=3;i<=n;i++){

        a = b;
        b = nextnum;
        nextnum = a + b;

        printf("%d ", nextnum);

    }// printf("%d", nextnum);

    return 0;
}