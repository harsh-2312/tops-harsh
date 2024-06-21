//q13 accept 5 numbers from user and check entered number is even or odd
//using of array

#include<stdio.h>

int main(){

    int i , a[20];

    printf("enter a number:");
    for(i=0;i<5;i++){
        scanf("%d",&a[i]);
    }

    for(i=0;i<5;i++){
        if(a[i]%2==0){
            printf("%d=even\n",a[i]);
        }
        else{
            printf("%d=odd\n",a[i]);
        }
    }


    return 0;
}