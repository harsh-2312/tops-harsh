//q23
//Accept month number and display month name
#include<stdio.h>
int main(){

int month;

printf("enter month number(1-12):");
scanf("%d", &month);

if(month ==  1){
    printf(" january\n");
}else if(month ==  2){
    printf(" february\n");
}else if(month ==  3){
    printf(" march\n ");
}else if(month ==  4){
    printf(" april\n");
}else if(month ==  5){
    printf("may\n ");
}else if(month ==  6){
    printf("june\n ");
}else if(month ==  7){
    printf("july\n ");
}else if(month ==  8){
    printf("august\n ");
}else if(month ==  9){
    printf("saptember\n ");
}else if(month ==  10){
    printf("october\n");
}else if(month ==  11){
    printf("november\n ");
}else if(month ==  12){
    printf("december\n");
}else{
    printf(" error");
}


    return 0;
}