// q4 
#include<stdio.h>
int main(){

    int num1, num2, result;
    char op;
 
    printf(" enter a operator ( +,-,*,/,%%) :");
     scanf("%c", &op);
    
    printf(" enter a num1 : ");
    scanf("%d", &num1);

    printf(" enter a num2 :");
    scanf("%d", &num2);

    

    switch(op){
        case('+'):result=num1+num2;
                 printf("result:%d\n",result);
                 break;
        case('-'):result=num1-num2;
                 printf("result:%d\n",result);
                 break;
        case('*'):result=num1*num2;
                 printf("result:%d\n",result);
                 break;
        case('/'):result=num1/num2;
                 printf("result:%d\n",result);
                 break;                           
        case('%'):result=num1%num2;
                 printf("result:%d\n",result);
                 break;  
      
}

return 0;
}