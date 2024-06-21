//q3
#include<stdio.h>
// WAP to check if the given year is a leap year or not.
int main(){

    int year;

    printf(" enter a year : ");
    scanf("%d", &year);

    if((( year % 4 == 0) && (year % 100!=0)) || ( year % 400 == 0)){
        printf(" its a leap year  \n");
    } else{
        printf(" its not leap  year\n");
    }
      return 0;
}