// q6 

#include<stdio.h>
int main(){
// Find the Character Is Vowel or Not
    char ch ;

    printf(" enter a character:");
    scanf("%c", &ch);


    if( ch == 'a' || ch =='A' || ch =='e' || ch == 'E' || ch == 'i' || ch == 'I' || ch == 'o' || ch == 'O' || ch == 'u' || ch == 'U'  ){
        printf("  character  is vowel  \n" , ch);

    } else{
        printf(" character   is consonant \n", ch);
    }
      return 0;
}