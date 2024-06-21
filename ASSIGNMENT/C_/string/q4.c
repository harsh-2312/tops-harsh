//q4 to count the total number of words in a string.

#include<stdio.h>
#include<string.h>


int main(){

    char str[100];
    int words=0,i;
    printf("enter string:");
    gets(str);

    for(i=0;str[i]!='\0';i++){
        if(str[i]==' ' && str[i+1] != ' '){
            words++;
        }
    }

    printf("total number of words:%d\n" , words+1);

    return 0;
}