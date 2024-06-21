//to read a sentence and replace lowercase characters with uppercase and vice versa.

#include<stdio.h>
#include<string.h>


int main()
{
 char str[20];
 int i;
 printf("\n enter a string:");
 gets(str);
 for(i=0;str[i]!='\0';i++)
 {
    // lowercase to uppercase
    if(str[i]>=97 && str[i]<=122)
    {
    	str[i]=str[i]-32;
    }
    // uppercase to lowercase
    else if(str[i]>=65 && str[i]<=90)
    {
    	str[i]=str[i]+32;
    }
 }
 printf(" %s",str);

 return 0;

}
