//q23
//1 + 2 + 3 + 4 + 5 + ... + n


#include<stdio.h>

int main(){

    int n , sum=0,i;

    printf(" enter a number:");
    scanf("%d", &n);

    for(i=1;i<=n;i++){
        sum+=i;
    }

    printf("sum:%d\n", sum);

   

    return 0;
}