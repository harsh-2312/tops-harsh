// q12
//WAP to find maximum number among 3 numbers using ternary operator
#include<stdio.h>

int main(){

int a , b, c, maxnum;

printf("enter a number: ");
scanf("%d%d%d" , &a, &b, &c);

 maxnum = ( a>b && a>c) ? (a) : ( (b>c && b>a) ? (b):(c));
 
  printf(" maximum number is :%d\n", maxnum);

return 0 ;

}