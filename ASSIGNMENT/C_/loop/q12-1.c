//q12x
//Program of Armstrong Number in C Using For Loop & While Loop
#include<stdio.h>

int main(){

    int n,num,r,ans=0;
// using while loop
    printf("enter number:");
    scanf("%d",&num);

    n=num;
    while(n>0){
     r= n%10;
     ans=ans+ r*r*r;
     n= n/10;
    }if(ans==num){
        printf("number is armstrong\n",num);

    }else{
        printf("number is not armstorng\n", num);
    }

    return 0;
}





