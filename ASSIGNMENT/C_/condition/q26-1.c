//q26
//Monday to Sunday using switch case
#include<stdio.h>
int main(){
int week;

printf(" enter week number (1-7):");
scanf("%d", &week);

switch(week){
    case 1 : printf(" monday\n");
    break;
    case 2 : printf(" tuesday\n");
    break;
    case 3 : printf(" wednesday\n");
    break;
    case 4 : printf(" thursday\n");
    break;
    case 5 : printf(" friday\n");
    break;
    case 6 : printf(" saturday\n");
    break;
    case 7 : printf(" sunday\n");
    break;
    default: printf("error\n");

    
}   


    return 0;
}
