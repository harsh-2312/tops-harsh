//q20

#include<stdio.h>

int main(){

int month;

printf(" enter a month (1-12):");
scanf("%d", &month);

if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12){

    printf(" 31 days\n");
}
else if( month == 4 || month == 6 || month == 9 || month == 11){

    printf(" 30 days\n");
}
else if( month == 2){
    printf(" 28 ,29 days\n");
}
else{

    printf(" invalid month\n");
}

printf(" thank you");

return 0;
}