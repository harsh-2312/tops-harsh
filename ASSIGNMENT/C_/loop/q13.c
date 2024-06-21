//q13
//calculate the Factorial of a Given Number using while loop
#include<stdio.h>

int main(){

int f=1, num , i=1;

printf(" enter a  num:");
scanf("%d", &num);

while(i <= num){

    f = f * i;
    i++;

}

printf("factorial %d is:%d\n ", num , f);
   

    return 0;
}