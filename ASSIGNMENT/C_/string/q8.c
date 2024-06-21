// count the total number of vowels or consonants in a string

 #include<stdio.h>
 #include<string.h>

 int main(){

    int vowel=0, consonants=0,i;
    char str[50];

    printf("enter string:");
    gets(str);

    for(i=0;str[i]!='\0';i++){

        if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u'||str[i]=='A'||str[i]=='E'||str[i]=='I'||str[i]=='O'||str[i]=='U'){
             vowel++;
        }
      
      else if((str[i]>=65&&str[i]<=90)||(str[i]>=97&&str[i]<=122)){
        consonants++;
      }
    }

    printf("vowel=%d\n", vowel);
    printf("consonants=%d\n", consonants);

    return 0;

 }