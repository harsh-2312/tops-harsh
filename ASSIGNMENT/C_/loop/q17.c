//q17
//.Calculate 5 numbers from user and calculate number of even and odd 

#include<stdio.h>
int main(){

    int i, num, sum=0,even=0,odd=0;

    printf("enter 5 number\n");
     
     i=1;
    while(i<=5){
        printf("number%d=",i);
        scanf("%d", &num);
        i++;
    

        if(num %2==0){
            even++;
        }else{
            odd++;
        }

    }
        printf("totel even=%d\n", even);
        printf("total odd=%d\n", odd);


    return 0;
}