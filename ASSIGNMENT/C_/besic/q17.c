//q17x
//17.Calculate person’s insurance premium based on salary

#include <stdio.h>

int main() {
    float salary,premiumRate=0.05, insurancePremium;

    printf(" enter salary:");
    scanf("%f", &salary);

    insurancePremium=salary * premiumRate;

    printf("insurance premium based  salary:%f\n", insurancePremium);



    return 0;
}
