//  Write a program to find the multiplication values and the cubic values using 
// inline function 

#include<iostream>
using namespace std;

class line{

    public:
    int mul(int a,int b){
        return a*b;

    }
    int cube(int a){
        return a*a*a;
    }

};
int main(){

    line l;
    int num1,num2;
    cout<<"enter a num 1:";
    cin>>num1;
    cout<<"enter a num2:";
    cin>>num2;
    cout<<endl<<"multiplication:"<<l.mul(num1,num2)<<endl;
    cout<<endl<<"cube num1:"<<l.cube(num1)<<endl;
    cout<<"cube num2:"<<l.cube(num2)<<endl;

}
