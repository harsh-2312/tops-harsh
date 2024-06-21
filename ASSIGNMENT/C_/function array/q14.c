//q14 Perform 2D matrix array

#include<stdio.h>

int main(){

    int i=0,j=0,arr[3][3];

    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            printf("enter array[%d][%d]:",i,j);
            scanf("%d",&arr[i][j]);
        }
    }
    printf("\nprinting the elements...........\n");
    for(i=0;i<3;i++){
        printf("\n");
        for(j=0;j<3;j++){
            printf("%d\t",arr[i][j]);
        }
    }


    return 0;
}