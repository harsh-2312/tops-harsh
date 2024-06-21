//q7
//WAP Find out length of string without using inbuilt function

#include<stdio.h>
int main(){

    char str[50];
    int i,length=0;

    printf("enter string:");
    scanf("%s",&str);

    for(int i=0;str[i]!='\0';i++){

        length++;

        
    }printf("length of strinf:%d\n",length);



    return 0;
}