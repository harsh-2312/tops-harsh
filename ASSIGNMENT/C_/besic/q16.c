//q16 
//16.Convert country’s name in abbreviate form


#include<stdio.h>
int main(){

    char cname[20];

    printf(" enter a country name:");
    scanf("%s",cname);

    printf("abbreviated fom: ");
    printf("%c%c%c",cname[0],cname[1],cname[2]);

    return 0;
}
