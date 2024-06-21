//q1
//Write a program to find out the max number from given array using function


#include<stdio.h>
 int main(){
   int n, arr[100];

    printf("enter 5 numbers\n");
    scanf("%d", &n);

    for(int i=1;i<=5;i++){
        printf("enter number%d:", i+1);
        scanf("%d", &arr[i]);
    }
    for(int i=1;i<=n;i++){
        if(arr[0]>arr[i]){
            arr[0]=arr[i];
        }
    }printf("max number:%d\n",arr[0]);

     return 0;

 }



// int main(){

//     int arr[]={ 25, 11, 7, 75, 56};

//     int length= sizeof(arr)/sizeof(arr[0]);

//     int max=arr[0];

//     for(int i=0;i<length;i++){
//         if(arr[i]>max){
//             max=arr[i];
//         }
//     }printf("max number is %d\n", max);


//     return 0;

// }