// Write a program to Mathematic operation like Addition, Subtraction, 
// Multiplication, Division Of two number using different parameters and 
// Function Overloading 

#include<iostream>
using namespace std;

class calculater{

    public:
    int a,b;

    int add(int a,int b){
        return a+b;
    }
    int sub(int a,int b){
        return a-b;
    }
    int mul(int a,int b){
        return a*b;
    }
    int div(int a,int b){
        if(b!=0){
        return a/b;
        }
        else{
            cout<<"Cannot divide by zero";
        }
    }

};
int main(){
    calculater c;
    int a,b;
    cout<<"enter num1:";
    cin>>a;
    cout<<"enter num2:";
    cin>>b;
    cout<<endl<<"addition:"<<c.add(a,b);
    cout<<endl<<"subtraction:"<<c.sub(a,b);
    cout<<endl<<"multiplication:"<<c.mul(a,b);
    cout<<endl<<"division:"<<c.div(a,b);


}