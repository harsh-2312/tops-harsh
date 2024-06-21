//q26 
//Convert temperature Fahrenheit to Celsius
//Celsius = ((Fahrenheit-32)*5)/9

#include<stdio.h>

int main(){

    float Fahrenheit, Celsius;

    printf(" enter Fahrenheit:");
    scanf("%f", &Fahrenheit);

    Celsius = ((Fahrenheit - 32)*5)/9;

    printf(" celsius is :%f \n ",Celsius );


    return 0;



}