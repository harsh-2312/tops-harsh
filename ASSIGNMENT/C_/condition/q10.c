// q 10

//WAP to check whether a number is negative, positive or zero.
#include<stdio.h>
int main(){

    int num;

    printf(" enter a number : ");
    scanf("%d", &num);


    if(num > 0){
        printf(" number is positive \n");
    } else if( num < 0){
        printf(" number is nagative \n");
    } else {
        printf(" number is zero  \n");
    }
      return 0;
}