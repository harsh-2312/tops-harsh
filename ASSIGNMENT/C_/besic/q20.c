//q20x
/*Accept monthly salary from the user and deduct 10% insurance premium,
10% loan installment find out of remaining salary*/

#include<stdio.h>

int main(){

    float monthlysalary, insurancePremium, installment, remainingsalary;

    printf(" enter salary:");
    scanf("%f", &monthlysalary);

    insurancePremium=0.10 * monthlysalary;
    printf("insurancepremium:%f\n", insurancePremium);

    installment=0.10 * monthlysalary;
    printf("installment:%f\n", installment);

    remainingsalary=( monthlysalary - insurancePremium ) - installment;
    printf(" remainingsalary:%f\n", remainingsalary);


    



    return 0;
}