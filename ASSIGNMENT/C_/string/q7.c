 //copy one string to another string.


 #include<stdio.h>
 #include<string.h>

 int main(){

    char str1[20],str2[20];
    
    printf("enter any string:");
    gets(str1);

    strcpy(str2,str1);

    printf("original string=%s\n", str1);
    printf("copy string=%s\n", str2);


    return 0;
 }