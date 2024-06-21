// q9 

#include<stdio.h>
int main(){
    char ch;

    printf(" enter a cheracter:");
    scanf("%c", &ch);


    if( ch >= 65 && ch <= 90 ){
        printf(" uppercase   \n" , ch);

    } else if ( ch >= 97 && ch <= 122 ){
        printf(" lowercase \n" , ch);

    } else if ( ch >= 48 && ch >= 52 ){
        printf(" number  \n" , ch);

     }else{
        printf(" symbol \n", ch);
        }
    
      return 0;
}