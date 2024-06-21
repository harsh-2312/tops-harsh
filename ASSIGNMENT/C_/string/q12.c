// to find the number of times a given word 'is' appears in the given string.

#include<stdio.h>
#include<string.h>

int main(){

    char str[50],worde[]= " is ";
    int i,j,ls,lw,chk,countw=0,temp;

    printf("enter string:");
    gets(str);
    ls=strlen(str);//string length
    lw=strlen(worde);

    for(i=0;i<ls;i++){
        temp=i;
        for(j=0;j<lw;j++){
            if(str[i]==worde[j]){
                i++;
            }
        }
        chk=i-temp;
        if(chk==lw)
            countw++;
            i=temp;
        
    }
    printf("occurrence = %d\n", countw);

    return 0;

}