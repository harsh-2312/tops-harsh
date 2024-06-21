//q6
//WAP to make addition, Subtraction and multiplication of two matrix using
//2-D Array

#include<stdio.h>

int main(){
   
   int row,col,r,c,arr1[2][2],arr2[2][2],sum[2][2],sub[2][2],mul[2][2];

   printf("enter the value of arry1:");
   for(int row=0;row<2;row++){
    for(int col=0;col<2;col++){
        scanf("%d",&arr1[row][col]);
    }
   }
   printf("enter the value of arry2:");
   for(int row=0;row<2;row++){
    for(int col=0;col<2;col++){
        scanf("%d",&arr2[row][col]);
    }
   }
   printf("\narra1:");
   for(int row=0;row<2;row++){
    printf("\n");
    for(int col=0;col<2;col++){
        printf("%d",arr1[row][col]);
    }
   }
   printf("\narra2:");
   for(int row=0;row<2;row++){
    printf("\n");
    for(int col=0;col<2;col++){
        printf("%d",arr2[row][col]);
    }
   }
   printf("\naddition arry\n");
   for( int row=0;row<2;row++){
    for(int col=0;col<2;col++){
        sum[row][col]=arr1[row][col]+arr2[row][col];
        //printf("\n the value of sum is:%d",sum[row][col]);
    }
   }
   for(int row=0;row<2;row++){
      printf("\n");
      for(int col=0;col<2;col++){
        printf("%d ",sum[row][col]);
      }
   }
   printf("\nsubtraction arry\n");
   for( int row=0;row<2;row++){
    for(int col=0;col<2;col++){
        sub[row][col]=arr1[row][col]-arr2[row][col];
        //printf("\n the value of sum is:%d",sum[row][col]);
    }
   }
   for(int row=0;row<2;row++){
      printf("\n");
      for(int col=0;col<2;col++){
        printf("%d ",sub[row][col]);
      }
   }
//    printf("\nmultiplication arry\n");
//    for( int row=0;row<2;row++){
//     for(int col=0;col<2;col++){
//         mul[row][col]=0;
//         for(int k=0;k<c;k++){
//             mul[row][col]=arr1[row][k]*arr2[k][col];

//         }
        
//     }
//    }
//    for(int row=0;row<2;row++){
//       printf("\n");
//       for(int col=0;col<2;col++){
//         printf("%d ",mul[row][col]);
//       }
//    }





    return 0;
}