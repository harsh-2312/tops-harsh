//q5  compare two strings without using string library function

#include<stdio.h>

int main(){

    char str1[50],str2[50];
    int i;

    printf("enter string1:");
    gets(str1);

    printf("enter string2:");
    gets(str2);

   for(i = 0; str1[i] == str2[i] && str1[i] == '\0'; i++);
		   
  	if(str1[i] < str2[i])
   	{
   		printf("\n str1 is Less than str2");
	}
	else if(str1[i] > str2[i])
   	{
   		printf("\n str2 is Less than str1");
	}
	else
   	{
   		printf("\n str1 is Equal to str2");
	}

    return 0;
}
