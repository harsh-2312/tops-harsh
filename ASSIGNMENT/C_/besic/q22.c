//q22
/*.Calculate compound interest (Compound Interest formula:
a. Formula to calculate compound interest annually is given by:
Amount= P(1 + R/100)t
b. Compound Interest = Amount – P*/
 
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
   printf("amount is = %f\n", amount);

    CI = amount - principle;
    printf("Compound Interest = %f\n", CI);



    return 0;
}