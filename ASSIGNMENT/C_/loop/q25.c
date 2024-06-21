//q25
// (1)+ (1+2) + (1+2+3) + (1+2+3+4) + ... + (1+2+3+4+...+n)


#include<stdio.h>

int main(){

    int n,i,j, sum,currentSum=0;

    printf(" enter a number:");
    scanf("%d", &n);

    for(i=0;i<=n;i++){
         sum=0;
        for(j=0;j<=i;j++){
            currentSum+=j;
            
        } sum+=currentSum;
        // sum+=currentSum;
    }

     printf("sum:%d\n", sum);

   

    return 0;
}