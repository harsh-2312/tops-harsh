//reverse a string and check that the string is palindrome or not

#include<stdio.h>
#include<string.h>

int main(){

    char str[50];
    int i,len,flag=0;

    printf("enter name:");
    scanf("%s",str);

    printf("reverse string:%s\n", strrev(str));

    len=strlen(str);

    for(i=0;i<len;i++){
        if(str[i] != str[len-i-1]){

            flag=1;
            break;
        }
    }
    if(flag=0){
        printf("%s is not a palindrome string", str);
    }
    else{
         printf("%s is a palindrome string", str);
    }

    return 0;


    
}