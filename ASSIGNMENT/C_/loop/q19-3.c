//q19-3
/*    
A
BC
DEF
GHIJ
KLMNO*/


#include<stdio.h>

int main(){

   char row,col,c='A';

    for(row=1;row<=5;row++){
        for(col=1;col<=row;++col){

            printf("%c",c);
            ++c;
        }
        printf("\n");
    }


    return 0;
}