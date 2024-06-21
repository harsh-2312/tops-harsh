//q14
//Accept 5 numbers from user and find those numbers factorials
#include<stdio.h>

int main(){

    int i, n,j;// factorial
    //  printf(" enter a num");
    //  scanf("%d", &n);

     for(i=0;i<=5;++i){
        printf("enter a num:");
        scanf("%d", &n);
         int f=1;
        for(j=1;j<=n;j++){

            f = f * j;
        }

      //  f = f * n;
        
        printf("factorial is:%d\n",f);
    }

    return 0;
}