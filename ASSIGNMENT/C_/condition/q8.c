// q8
#include<stdio.h>
int main(){
    float height;

    printf(" enter a height:");
    scanf("%f", &height);


    if( height < 150.0){
        printf(" this person short  \n" , height);

    } else if ( (height >= 150.0 && height <= 170.0) ){
        printf("this person avrage \n" , height);

    } else{
        printf(" this person tall \n", height);}
    
      return 0;
}