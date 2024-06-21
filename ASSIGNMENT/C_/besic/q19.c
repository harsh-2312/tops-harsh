//q19
// C program to calculate Compound Interest


#include <stdio.h>
#include <math.h>

 int main(){

    float principle, rate, time, CI, amount; // compound interest

    
    printf("Enter principle (amount): ");
    scanf("%f", &principle);

    printf("Enter time: ");
    scanf("%f", &time);

    printf("Enter rate: ");
    scanf("%f", &rate);

    
    amount = principle* (pow((1 + rate / 100), time));
   // printf("amount is = %f", amount);

    CI = amount - principle;
    printf("Compound Interest = %f", CI);



    return 0;
}