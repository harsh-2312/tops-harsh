//q21 
/*Accept 3 numbers from user using while loop and check each numbers
palindrome*/



#include<stdio.h>

int main(){

   int num , reverse=0, rem, temp,i;
   

   for(i=1;i<=3;i++){
   printf("enter a number:");
   scanf("%d", &num);

   temp=num;

   do{
    rem = temp % 10;
    reverse = reverse * 10 + rem;
    temp /= 10;

   }while(temp!=0);
   printf("revers number:%d\n",reverse);



   if( reverse==num){
    printf("%dnumber is palindrome\n ", num);
   }
    else{ 
        printf("%d not palindrome number\n", num);
    }
   }

    return 0;
}