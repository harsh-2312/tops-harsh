//q11
//Accept 5 names from user at run time

#include<stdio.h>

int main() {
    char a[5][100];
    int r;
    
    for(r=0;r<5;r++)
    {
        printf("enter name:");
        scanf("%s",&a[r]);
        
    }
    for(r=0;r<5;r++)
    {
        printf("%s\n",a[r]);
    }
    return 0;
}


