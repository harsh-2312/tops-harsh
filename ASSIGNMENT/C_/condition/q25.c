//q24
//Accept the input month number and print number of days in that 
#include<stdio.h>

int main(){

    int month;

    printf("enter month number(1-12):");
    scanf("%d", &month);


    if(month ==  1){
    printf("31 days \n");
     }else if(month ==  2){
    printf("28, 29 days \n");
     }else if(month ==  3){
    printf("31 days \n ");
      }else if(month ==  4){
    printf("30 days\n");
     }else if(month ==  5){
    printf("31 days\n ");
     }else if(month ==  6){
    printf("30 days\n ");
     }else if(month ==  7){
    printf("31 days\n ");
     }else if(month ==  8){
    printf("31 days\n ");
    }else if(month ==  9){
    printf("30 days\n ");
     }else if(month ==  10){
    printf("31 days\n");
     }else if(month ==  11){
    printf("30 days\n ");
      }else if(month ==  12){
    printf("31 days\n");
     }else{
    printf(" error");
     }

    return 0;

}