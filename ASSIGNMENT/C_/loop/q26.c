//26x
//1/2 - 2/3 + 3/4 - 4/5 + 5/6 - ...... n

#include<stdio.h>

int main(){

    
    float n, sum=0;

    printf("enter number:");
    scanf("%f",&n);
    for(int i=1;i<=n;i++){
        // printf("enter number");
        // scanf("%d",&n);
        if(i%2==1){
            sum+=(float)i/(i+1);
            printf("%d/%d - ",i,i+1);

        }
        else{
            sum-=(float)i/(i+1);
            printf("%d/%d + ",i,i+1);
        }
    }printf(" = %.2f",sum);


   // return  0;
}