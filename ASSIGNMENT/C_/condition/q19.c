//q19
/*Write a program in C to calculate and print the electricity bill of a given
customer. The customer ID, name, and unit consumed by the user should
be captured from the keyboard to display the total amount to be paid to the
customer. The charge are as follow*/

#include<stdio.h>

int main(){
   // char name;
    int id, unit;
    float amount,charge,total_amt,surcharge;
    char name;

    printf("custuomer name:");
    scanf("%s", &name);

    printf("custuomer id:");
    scanf("%d", &id);

    printf("unit:");
    scanf("%d", &unit);

    if(unit < 350){

        amount= unit * 1.20;

    }else if(unit >= 350 && unit < 600){
       
        amount= unit * 1.50;

    }else if (unit >= 600 && unit < 800){

        amount= unit * 1.80;

    }else{

        amount= unit * 2.00;
    }

    if(amount > 800){

        surcharge= amount * 0.18;
        total_amt= surcharge + amount;
    }if(total_amt< 256){
        total_amt=256;
    }




    printf("total amout:%f\n", total_amt);



    return 0;

}