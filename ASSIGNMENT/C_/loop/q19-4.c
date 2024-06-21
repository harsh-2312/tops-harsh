//q19-4
/*
A
AB
ABC
ABCD
ABCDE*/


#include<stdio.h>

int main(){

   int row,col;
   char ch ='A';

    for(row=1;row<=5;row++){
        for(col=1;col<=row;col++){

            printf("%c",ch++);
            

            
        }
        
        printf("\n");
        ch='A';

    }


    return 0;
}
