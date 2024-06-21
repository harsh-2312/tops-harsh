// q17 

#include<stdio.h>
 int main(){

 int angle1, angle2, angle3, sum;


 printf(" enter angle1 :");
 scanf("%d", &angle1);

 printf(" enter angle2 :");
 scanf("%d", &angle2);

 printf(" enter angle3 :");
 scanf("%d", &angle3);

sum = angle1 + angle2 + angle3;

 if ( sum == 180  && angle1 > 0 && angle2 > 0 && angle3 > 0){

    printf(" triangale is valid");

 }else{
     printf(" triangle is not valid");
 }
    return 0;
 }
