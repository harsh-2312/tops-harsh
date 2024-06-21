//q22
//C Program to Reverse a Number Using FOR Loop


#include<stdio.h>

int main(){

int num , reverse=0 , temp , rem;//remainde

    printf(" enter a number:");
    scanf("%d", &num);
   temp=num;
    for(;temp!=0;temp/=10){

        rem= temp % 10;
        reverse= reverse * 10 + rem;
    }

printf("revers num =  %d\n",reverse);

    return 0;
}