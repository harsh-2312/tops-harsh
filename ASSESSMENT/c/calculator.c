//calculator

#include<stdio.h>

int add(int a,int b);
int sub(int a,int b);
int mul(int a,int b);
int div(int a,int b);


int main(){
    int choice, result,a,b;
    char op;

    do{

    printf("\n-------------menu--------------\n");
    printf("1.additon\n");
    printf("2.subtracton\n");
    printf("3.multipication\n");
    printf("4.division\n");

    printf("\nenter your choice (1-4):");
    scanf("%d", &choice);

    if(choice>=4){
        printf("invelid choice!!!!\n-----------------------------------------");
        return 0;
    }

    printf("\nenter first number :");
    scanf("%d", &a);

    printf("enter first number :");
    scanf("%d", &b);
            
    switch (choice){
    
        case 1: result= add(a , b);
            printf("\nadditon = %d\n", result);
        break;
        case 2: result= sub(a , b);
            printf("\nsubtracton = %d\n", result);
        break;
        case 3: result= mul(a , b);
            printf("\nmultipicaton = %d\n", result);
        break;
        case 4: result= div(a , b);
            printf("\ndiviston = %d\n", result);
        break;

    default:printf("Invalid choice! Please enter a number between 1 and 4.\n");
        break;
    }

    printf("---------------------------------\n");

    printf("\nDo you want to perform another calculation? (y/n):");
    scanf("%s", &op);

    }while(op =='y' || op =='Y');

    printf("----------------thank you-------------------\n");
 
    
    return 0;
}

int add(int a,int b){
    return a+b;
}
int sub(int a,int b){
    return a-b;
}
int mul(int a,int b){
    return a*b;
}
int div(int a,int b){
    if(b != 0){
        return a/b;
    }else{
        printf("Error! Division by zero.\n");
    }
    
    
    return a/b;
}
