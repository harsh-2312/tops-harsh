//q6.  count the total number of alphabets, digits and special characters in a string. 

#include<stdio.h>
#include<string.h>

int main(){

    int alpha=0,digit=0,sp=0,i;
    char str[50];

    printf("enter your string:");
    gets(str);

    for(i=0;str[i];i++){

    if((str[i]>='a' && str[i]<='z')|| (str[i]>='A'&& str[i]<='Z')){

        alpha++;
    }
    else if(str[i]>='0' && str[i]<='9'){
        digit++;
    }
    else{
        sp++;
    }

    }

    printf("alphabets=%d\n", alpha);
    printf("digits=%d\n", digit);
    printf("special characters=%d\n", sp);

    return 0;
}