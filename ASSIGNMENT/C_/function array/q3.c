//q3
//WAP to find reverse of string using recursion

#include<stdio.h>
#include<string.h>

void revstr(char str[]){
int i , length ,temp;

length = strlen(str);


for(i=0;i<length/2;i++){

    temp=str[i];
    str[i]=str[length-i-1];
    str[length-i-1]=temp;
}
}

int main(){

    char str[50];

    printf("enter string:");
    gets(str);
    
    //printf("reverse string:%s\n",str);
    revstr(str);
    printf("reverse string:%s\n",str);
    return 0;
}

