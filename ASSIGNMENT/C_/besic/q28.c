//q28
//Convert years into days and months

#include<stdio.h>

int main(){

    int year,day,month;

    printf("enter year:");
    scanf("%d", &year);

    day= year * 365;
    printf("day:%d\n", day);

    month= year * 12;
    printf("month:%d\n", month);


    return 0;

}