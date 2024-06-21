//q30
//WAP to convert years into days and days into years

#include<stdio.h>

int main(){
    int year,days;
    //convert years into days

    printf("enter year:");
    scanf("%d", &year);

    days= year * 365;

    printf(" days= %d",days);

 //days into years

  printf("\nenter days:");
    scanf("%d", &days);

    year= days / 365;

    printf(" days= %d",year);



    return 0;
}