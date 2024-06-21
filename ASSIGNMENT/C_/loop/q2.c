//q2 
//WAP to accept 5 numbers from user and display all numbers
#include<stdio.h>

int main(){
     
     int num[50],i;
     

     printf("enter a 5 number:\n");
     for(i=0;i<5;i++){
      scanf("%d", &num[i]);
     }

     for(i=0;i<5;i++){
      printf(" %d ", num[i]);
     }  
     return 0; 
 
}