// q7

//Accept marks from user and check pass or fail
#include<stdio.h>
int main(){
    int marks;

    printf(" enter a marks:");
    scanf("%d", &marks);


    if( marks >= 35 ){
        printf("  you have passed \n" , marks);

    } else{
        printf(" you have failled \n" , marks);
    }
      return 0;
}