//q16 
/*Write a C program to read temperature in centigrade and display a suitable
message according to the temperature state below:
Temp < 0 then Freezing weather
Temp 0-10 then Very Cold weather
Temp 10-20 then Cold weather
Temp 20-30 then Normal in Temp
Temp 30-40 then Its Hot
Temp >=40 then Its Very Hot*/
#include<stdio.h>

int main(){
 
 
  int temperature;

  printf(" enter temperature :");
  scanf("%d", &temperature );


  if(temperature < 0 ){
    printf(" freezing weather \n");

  }else if( temperature >= 0 && temperature <=10 ){

    printf(" weather is very cold \n");

  }else if( temperature  > 10 && temperature <= 20  ) {

    printf(" weather is cold \n");

  }else if( temperature  > 20 && temperature <= 30 ){

    printf(" weather is normal temp \n");

  }else if( temperature  > 30 && temperature <= 40 ){

    printf(" weather is hot \n");
  }else {
    printf(" weather is very hot \n");
  }
   printf(" thank you \n");
    return 0;
}