// Write a C++ Program to illustrates the use of Constructors in multilevel 
// inheritance 

#include<iostream>
using namespace std;

class A{
    public:
    A(){
        cout<<"harsh limbachiy"<<endl;
    }
};
class B : public A{
    public:
    B(){
        cout<<"age:22"<<endl;
    }
};
class C : public B{
    public:
    C(){
        cout<<"city:surat"<<endl;
    }
};
int main(){
    C c;
    
}