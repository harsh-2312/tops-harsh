//q8
//Write a program to find out the max from given number 
    
#include<stdio.h>

int main(){

    int num,max=0,i,n;

    printf("enter 4 number:");
    scanf("%d",&num);

    for(i=1;i<=4;i++){
        n=num%10;
        num=num/10;

       

        if(num>max){
            max=n;
        }
    }
    printf("max num:%d\n",max);




    return 0;
}