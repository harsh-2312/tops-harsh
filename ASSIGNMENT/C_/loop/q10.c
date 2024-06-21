//q10
//.Write a program you have to make a summation of first and last Digit.
#include<stdio.h>

int main(){

   int num , sum=0, firstdigit , lastdigit;

   printf(" enter a number:");
   scanf("%d", &num);

   lastdigit = num % 10;

   firstdigit = num;

   while(num >= 10){

    num = num / 10;
    //sum = sum + num;
   }
    firstdigit = num;
   sum = firstdigit + lastdigit;

   printf("sum of first & last num:%d\n", sum);


    return 0;
}