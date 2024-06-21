//q24
//Accept 5 employees name and salary and count average and total salary

#include<stdio.h>

int main(){

    int s1,s2,s3,s4,s5,average,total;
    char ch;

    printf("enter name:");
    scanf("%s", &ch);

    printf("enter salary:");
    scanf("%d", &s1);

    printf("enter name:");
    scanf("%s", &ch);

    printf("enter salary:");
    scanf("%d", &s2);

    printf("enter name:");
    scanf("%s", &ch);

    printf("enter salary:");
    scanf("%d", &s3);

    printf("enter name:");
    scanf("%s", &ch);

    printf("enter salary:");
    scanf("%d", &s4);

    printf("enter name:");
    scanf("%s", &ch);

    printf("enter salary:");
    scanf("%d", &s5);


    

     total=s1+s2+s3+s4+s5;
    //average=total/5;
     printf(" total:%d\n",total);
   
      average=total/5;
    printf("average:%d\n",average);



    return 0;

}
