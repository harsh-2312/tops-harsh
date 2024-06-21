//q2  separate individual characters from a string.


#include<stdio.h>
#include<string.h>

int main(){

    char string[100];

    printf("enter string name:");
   // scanf("%s", string);
   gets(string);
   

    int length=0;

   while(string[length]!='\0'){
         length++;
   }
    
     printf("individual characters\n");
    for(int i=0; i < length; i++){
        printf("%c ", string[i]);
    }
    return 0;
}

// int main()  
// {  
//     char string[] = "characters";  
          
//     //Displays individual characters from given string  
//     printf("Individual characters from given string:\n");  
      
//     //Iterate through the string and display individual character  
//     for(int i = 0; i < strlen(string); i++){  
//         printf("%c ", string[i]);  
//     }  
          
//     return 0;  
// }  
