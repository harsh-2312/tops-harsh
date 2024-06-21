// find the maximum number of characters in a string.

#include<stdio.h>
#include<string.h>

int main(){

    int count=0,maxcount=0,i,j;
    char maxch,str[50];

    printf("enter string:");
    gets(str);

    for(i=0;str[i]!='\0';i++){
        count=0;
        for(j=0;str[j]!='\0';j++){
            if(str[i]==str[j]){
                count++;
            }
        }if(maxcount<count){
            maxcount=count;
            maxch=str[i];

        }
    
    }
    printf("the character %c repetade maximum of %d time\n", maxch,maxcount);
    


    return 0;
}