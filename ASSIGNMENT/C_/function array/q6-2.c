//multiplication

#include<stdio.h>

int main(){

    int row,col,r,c,arr1[50][50],arr2[50][50],mul[50][50];

    printf("enter the value of row:");
    scanf("%d",&r);
    printf("enter the value of col:");
    scanf("%d",&c);

    printf("enter the value of arr1:");
    for(row=0;row<r;row++){
        for(col=0;col<c;col++){
            scanf("%d", &arr1[row][col]);
        }
    }
    printf("enter the value of arr2:");
    for(row=0;row<r;row++){
        for(col=0;col<c;col++){
            scanf("%d",&arr2[row][col]);
        }
    }
    printf("arry1:");
    for(row=0;row<r;row++){
        printf("\n");
        for(col=0;col<c;col++){
        printf("%d",arr1[row][col]);
    }
    }
    printf("arry2:");
    for(row=0;row<r;row++){
        printf("\n");
        for(col=0;col<c;col++){
            printf("%d",arr2[row][col]);
        }
    }
    printf("multiply:\n");
    for(row=0;row<r;row++){
        for(col=0;col<c;col++){
            mul[row][col]=0;
            for(int k=0;k<c;k++){
                mul[row][col]+=arr1[row][k]*arr2[k][col];
            }
        }
    }
    for(row=0;row<r;row++){
        printf("\n");
        for(col=0;col<c;col++){
            printf(" %d ",mul[row][col]);
        }
    }





return 0;

}