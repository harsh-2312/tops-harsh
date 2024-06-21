//q26-2 Vowel or Consonant using switch case

#include<stdio.h>
int main(){
char ch;

printf(" enter ch:");
scanf("%s", &ch);

switch(ch){
    case  'a': printf(" vowel\n");
    break;
    case  'e': printf(" vowel \n");
    break;
    case  'i': printf(" vowel \n");
    break;
    case 'o' : printf(" vowel\n");
    break;
    case  'u': printf(" vowel \n");
    break;
    case  'A': printf(" vowel\n");
    break;
    case  'E': printf(" vowel \n");
    break;
    case  'I': printf(" vowel \n");
    break;
    case  'O': printf(" vowel \n");
    break;
    case  'U': printf(" vowel \n");
    break;
    default: printf(" consonant\n");

    
}   


    return 0;
}