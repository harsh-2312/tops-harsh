//q11 WAP to accept 5 numbers from user and display in reverse order using for
//loop and array

#include<stdio.h>


int main()  
{  
    int a[5], i;  
  
    printf("Enter 5 integer numbers\n");  
    for(i = 0; i < 5; i++)  
        scanf("%d", &a[i]);  
  
    printf("revers number:\n");  
    for(i = 4; i >= 0; i--)  
        printf("%d\n ", a[i]);  
  
    return 0;  
}  