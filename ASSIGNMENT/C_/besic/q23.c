//q23
//WAP to calculate swap 2 numbers with using of multiplication and division.

#include<stdio.h>

int main(){

    int a , b;
 // Without Using Third Variable
    printf(" enter fist num  and second num:");
    scanf(" %d %d", &a,&b);
    printf("Before Swapping *\nFirst num = %d\nSecond num = %d\n",a , b);
    a= a*b;
    b= a/b;
    a= a/b;

    printf("after swapping*\nfirst num= %d\nsecond num= %d\n",a , b);


    return 0;
}