//q15 
//15.Convert school’s name in abbreviated for

#include<stdio.h>
int main(){

    char fname[20],mname[20],lname[20];

    printf(" enter a school name:");
    scanf("%s %s %s",fname ,mname ,lname);

    printf("abbreviated fom: ");
    printf("%c. %c. %s",fname[0], mname[0], lname);

    return 0;
}


