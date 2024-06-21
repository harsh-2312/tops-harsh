// q5

#include<stdio.h>
int main(){
// Check Number Is Positive or Negative
    int number;

    printf(" enter a number:");
    scanf("%d", &number);


    if( number >= 0 ){
        printf("  numner is positive \n" , number);

    } else{
        printf(" number is negative  \n" , number);
    }
      return 0;
}