//q9 Write a program of structure employee that provides the following
//    a. information -print and display empno, empname, address
//     andage
//    b. Write a program of structure for five employee that
//   provides the following information -print and display
//   empno, empname, address andage

#include<stdio.h>

struct employes{
    int no,age;
    char name[20],addres[50];
};

int main(){
    struct employes e[5];

    printf("------------------enter employes details--------------------\n");
    for(int i=0;i<5;i++){
        printf("employe no:");
        scanf("%d", &e[i].no);
        printf("employe name:");
        scanf("%s", &e[i].name);
        printf("employe address:");
        scanf("%s", &e[i].addres);
        printf("employe age:");
        scanf("%d", &e[i].age);
       // scanf("%d %s %s %d",&e[i].no,&e[i].name,&e[i].addres,&e[i].age);
       printf("\n");

    }
    printf("\n-------------------employes details--------------------------\n");
    for(int i=0;i<5;i++){
        printf("\nemploye number:%d",e[i].no);
        printf("\nemploye name:%s",e[i].name);
        printf("\nemploye addres:%s",e[i].addres);
        printf("\nemploye agr:%d",e[i].age);

        printf("\n");

    }

    return 0;

}
    