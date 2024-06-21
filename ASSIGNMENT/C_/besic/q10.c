// q10
#include <stdio.h>
#include<math.h>

int main() {

// 10.find the area of a rectangular prism formula : A=2(wl+hl+hw)


int length, width, height , area;

printf("enter length :");
scanf("%d", &length);

printf("enter width :");
scanf("%d", &width);

printf("enter height :");
scanf("%d", &height);


printf("area of a rectangular prism is : %d \n", area = 2 * (width * length + height * length + height * width) );
    return 0;
}