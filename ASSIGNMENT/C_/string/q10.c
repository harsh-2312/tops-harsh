// extract a substring from a given string 


#include<stdio.h>
#include<string.h>
 
int main(){

   char string[1000], sub[1000];
   int position, length, c = 0;
 
   printf("Input a string:");
   gets(string);
 
   printf("Enter the position:");
   scanf("%d", &position);

   printf("Enter the length:");
   scanf("%d", &length);
 
   while (c < length) {
      sub[c] = string[position+c-1];
      c++;
   }
   sub[c] = '\0';
 
   printf("Required substring is:%s\n", sub);
 
   return 0;
}