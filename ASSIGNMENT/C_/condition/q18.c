//q18 

#include<stdio.h>

int main(){
          //costprice, selingprice, 
    int cp, sp, profit, loss;

    printf(" enter costprice:");
    scanf("%d",&cp);

    printf(" enter selingprice:");
    scanf("%d", &sp);

    if( sp > cp){

        profit = sp - cp;
        printf("profit :%d\n", profit);

    } else if( sp < cp){

        loss = cp - sp;
        printf("loss :%d\n", loss);

    } else{

        printf("no profit , no loss");

    }

    return 0;
}