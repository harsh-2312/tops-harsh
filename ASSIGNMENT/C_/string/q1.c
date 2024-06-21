//q1 Write a program in C to find the length of a string without using library
//functions

#include<stdio.h>
#include<string.h>

int main(){

    char str[50];
    int i,length=0;

    printf("enter a string:");
    //scanf("%s",&str);
    gets(str);
    for(i=0;str[length]!='\0';i++){
        length++;
    }

    printf("length of string is:%d\n",length);


    return 0;
}
