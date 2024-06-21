//q17 WAP to show difference between Structure and Union

#include<stdio.h>

union student{
    int id;
    char name;
    float pr;
}s1,s2;

int main(){

    printf("studant detalis.......\n");
    printf("enter studant id s1\n");
    scanf("%d", &s1.id);
    printf("enter studant name s1\n");
    scanf("%s", &s1.name);
    printf("enter studant percent s1\n");
    scanf("%f", &s1.pr);
    printf("enter studant id s2\n");
    scanf("%d", &s2.id);
    printf("enter studant name s2\n");
    scanf("%s", &s2.name);
    printf("enter studant percent s2\n");
    scanf("%f", &s2.pr);
    printf("\nenter student detailils:\n");
    printf("\ndetails of student 1:\n%d \n%s \n%f",s1.id,s1.name,s1.pr);
    printf("\ndetails of student 2:\n%d \n%s \n%f",s2.id,s2.name,s2.pr);
    
    return 0;
}



