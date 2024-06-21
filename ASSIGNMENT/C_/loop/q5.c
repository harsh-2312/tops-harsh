//q5
//WAP to print factorial of given number
#include<stdio.h>

int main(){

    int i, n, f=1;// factorial
    printf(" enter a num");
    scanf("%d", &n);

    for(i=1;i<=n;i++){

        f = f * i;
        
        printf(" factorial is %d :%d\n",n ,f);
    }

    return 0;
}
