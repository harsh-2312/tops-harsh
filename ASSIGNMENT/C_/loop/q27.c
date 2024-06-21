//q27
//1 2 3 6 9 18 27 54...

#include<stdio.h>

int main(){

    int i,n1=1,n2=2,n=10;
    printf("%d %d" ,n1, n2);
    for(i=3;i<=n;i++){
        if(i%2==1){
            n1=n1*3;
            printf(" %d ",n1);
        }else{
            n2=n2*3;
            printf(" %d ",n2);
        }
    }
 return 0;

}