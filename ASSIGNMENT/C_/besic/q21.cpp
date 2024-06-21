//q21


// #include<stdio.h>

// int main(){

//     int a , b, c;
//  //Using Third Variable
//     printf(" enter fist num  and second num:");
//     scanf(" %d %d", &a,&b);
//     printf("Before Swapping *\nFirst num = %d\nSecond num = %d\n",a , b);
//     c=a;
//     a=b;
//     b=c;
//     printf("after swapping*\nfirst num= %d\nsecond num= %d\n",a , b);


//     return 0;
// }



#include<stdio.h>

int main(){

    int a , b;
 // Without Using Third Variable
    printf(" enter fist num  and second num:");
    scanf(" %d %d", &a,&b);
    printf("Before Swapping *\nFirst num = %d\nSecond num = %d\n",a , b);
    a= a+b;
    b= a-b;
    a= a-b;

    printf("after swapping*\nfirst num= %d\nsecond num= %d\n",a , b);


    return 0;
}