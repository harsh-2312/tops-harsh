// using for loop
#include<stdio.h>
int main(){

    int n,num,r,ans=0;
// using for loop
    printf("enter number:");
    scanf("%d",&num);

   
    for(n=num;n>0;n=n/10){
     r= n%10;
     ans=ans+ r*r*r;
     
    }if(ans==num){
        printf("number is armstrong\n",num);

    }else{
        printf("number is not armstorng\n", num);
    }

    return 0;
}
