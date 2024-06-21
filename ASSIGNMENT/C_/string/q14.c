// to combine two strings manually

#include<stdio.h>
#include<string.h>

int main(){

    int i,j;
    char str1[20],str2[20];

    printf("enter string 1:");
    gets(str1);

    printf("enter string 2:");
    gets(str2);

    for(i=0;str1[i]!='\0';i++);

        for(j=0;str2[j]!='\0';j++){

            str1[i]=str2[j];
            i++;
          
        }
     
    
    str1[i]= '\0';

    printf("combine strint is:%s\n", str1);



    return 0;
}