//q24
//(1*1) + (2*2) + (3*3) + (4*4) + (5*5) + ... + (n*n)


#include<stdio.h>

int main(){

    int n , sum=0,i;

    printf(" enter a number:");
    scanf("%d", &n);

    for(i=1;i<=n;i++){
        sum+=i * i;
    }

    printf("sum:%d\n", sum);

   

    return 0;
}