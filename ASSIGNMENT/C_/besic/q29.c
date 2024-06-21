//q29
//.Convert minutes into seconds and hours

#include<stdio.h>

int main(){
    int mint,sec,hours;

    printf("enter minute:");
    scanf("%d", &mint);

    sec= mint * 60;
    hours= mint / 60;

    printf(" second= %d",sec);
    printf(" hours= %d",hours);




    return 0;



}

