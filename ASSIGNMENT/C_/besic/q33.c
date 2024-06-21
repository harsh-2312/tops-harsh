//q33
//.C Program to Read Integer and Print First Three Powers (N^1, N^2, N^3)


#include<stdio.h>
#include<math.h>
int main(){
    int num;

    printf(" enter number:");
    scanf("%d", &num);

    printf("sum is %d ,%d ,%d  \n",num, num * num , num * num * num);

    
    return 0;



}
// 2nd
// int main()
// {
	
// 	int num, a, b, c;
// 	printf("enter Number:");
// 	scanf("%d", &num);
// 	a = pow(num, 1);
// 	b = pow(num, 2);
// 	c = pow(num, 3);
	
// 	printf(" sum is %d  ,%d  ,%d \n", a, b, c);
// 	return 0;
// }
