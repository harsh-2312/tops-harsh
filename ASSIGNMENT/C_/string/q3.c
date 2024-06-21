//q3 to print individual characters of a string in reverse order

#include<stdio.h>
#include<string.h>

int main(){

    
char str[100];
int length=0;

printf("enter string:");
gets(str);

length=strlen(str);

for(str[length]!='\0';length>=0;length--){
    printf("%c ", str[length]);
}printf("\n");

    return 0;
}