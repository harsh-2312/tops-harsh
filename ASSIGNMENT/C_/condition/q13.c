// q13 
// find minimum number among 3 numbers using ternary operator


#include<stdio.h>

int main(){

int a , b, c, minimum;

printf("enter a number: ");
scanf("%d%d%d" , &a, &b, &c);

 minimum = ( a<b && a<c) ? (a) : ( (b<c && b<a) ? (b):(c));
 
  printf(" maximum number is :%d\n", minimum);

return 0 ;

}