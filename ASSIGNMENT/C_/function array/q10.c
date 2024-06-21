//q10 WAP to perform Palindrome number using for loop and function

#include<stdio.h>

int palindrome(int num){

int temp,rem,rev=0,i;

for(i=num;i>0;){
     rem=i %10;
     rev=rev*10+rem;
     i=i/10;

}

if(rev==num){
    return 0;
}
else{
    return 1;
}
}
int main(){
    int num;

    printf("enter number:");
    scanf("%d", &num);

    if(palindrome(num)==0){
        printf("%d is palindrom\n",num);

    }else{
         printf("%d is not palindrom\n",num);

    }
    return 0;
}

// temp=num;
// while(num!=0){          
//     rem=num %10;
//     rev=rev*10+rem;
//     num=num/10;
// }

