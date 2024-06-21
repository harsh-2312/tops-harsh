//q32
//Accept 2 numbers and find out its sum check it size

#include<stdio.h>

int main(){

    int a , b, sum;

    printf(" enter num:");
    scanf("%d", &a);

    printf(" enter num:");
    scanf("%d", &b);

    sum= a + b;

    printf(" sum is:%d\n", sum);

    printf("sum size is:%d\n",sizeof(sum));



    return 0;
}