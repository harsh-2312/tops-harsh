//q1
//Write a C program to accept twointegers andcheck whether they are equalor not

#include<stdio.h>
int main(){
    int a, b;

    printf(" enter a num:");
    scanf("%d", &a);

    printf(" enter a num:");
    scanf("%d", &b);


    if(a==b){
        printf(" they are equal\n");

    } else{
        printf(" not equal\n");
    }
      return 0;
}