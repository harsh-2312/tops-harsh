//  Write a program to find the max number from given two numbers 
// using friend function

#include<iostream>
using namespace std;

class number{
    private:
    int a,b;
    public:
    void data(){
        cout<<"num1:";
        cin>>a;
        cout<<"num2:";
        cin>>b;
    }
friend void maxnum(number& n);
};
void maxnum(number& n){
    if(n.a>n.b){
        cout<<endl<<"max number:"<<n.a;
    }
    else{
        cout<<endl<<"max number:"<<n.b;
    }
}
int main(){
    number n;
    n.data();
    maxnum(n);
}
