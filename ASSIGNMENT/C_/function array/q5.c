//q5
//WAP to take two Array input from user and sort them in ascending or
//descending order as per users choice

#include<stdio.h>
int main(){



 int a[100],n,i,j;

 printf("arry size:");
 scanf("%d",&n);

 printf("enter elements:");
 for(int i=0;i<n;i++){
    scanf("%d",&a[i]);
 }

 for(int i=0;i<n;i++){// loop for ascending
    for(int j=0;j<n;j++){
        if(a[j]>a[i]){

        int tamp=a[i];
            a[i]=a[j];
            a[j]=tamp;
                       
        }
    }
 }printf("\n\nascending:");
      for(int i=0;i<n;i++){
        printf(" %d ",a[i]);
      }

 for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
         if(a[j]<a[i]){
            int temp=a[i];
                a[i]=a[j];
                a[j]=temp;

        }
    }

 }printf("\n\ndesending:");
    for(int i=0;i<n;i++){
        printf(" %d ",a[i]);
    }

 return 0; 
 getch();


}

