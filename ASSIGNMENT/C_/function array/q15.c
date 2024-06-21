//q15 .Store 5 numbers in array and sort it in ascending order

#include<stdio.h>



#include<stdio.h>
int main(){



 int a[100],n,i,j;

//  printf("arry size:");
//  scanf("%d",&n);

 printf("enter elements:");
 for(int i=0;i<5;i++){
    scanf("%d",&a[i]);
 }

 for(int i=0;i<5;i++){// loop for ascending
    for(int j=0;j<5;j++){
        if(a[j]>a[i]){

        int tamp=a[i];
            a[i]=a[j];
            a[j]=tamp;
                       
        }
    }
 }printf("\n\nascending:");
      for(int i=0;i<5;i++){
        printf(" %d ",a[i]);
      }
}

