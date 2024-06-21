// q14

// find the largest of three numbers.

#include<stdio.h>
int main(){

int n1, n2, n3;

printf("enter a number: \n");
scanf("%d%d%d" , &n1, &n2, &n3);

 if( n1 >= n2 && n1 >= n3){
printf("%d is  the largest number \n", n1);
 }if( n2 >= n1 && n2>= n3){

    printf("%d is the largest numbar \n",n2);

 } if( n3 >= n1 && n3 >= n2){
     printf("%d is the largest number \n", n3);
 }

return 0 ;

}