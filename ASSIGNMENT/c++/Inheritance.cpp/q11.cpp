//  Write a program to calculate the area of circle, rectangle and triangle 
// using Function Overloading 
// Rectangle: Area * breadth 
// Triangle: ½ *Area* breadth 
// Circle: Pi * Area *Area 

#include<iostream>
using namespace std;

class area{
    public:
    int a,b;
    public:
    void dete(){
        cout<<"enter area:";
        cin>>a;
        cout<<"enter breadth:";
        cin>>b;
    }
};
class calculat : public area{
    public:
    int rectangal(int a,int b){
        return a * b;
    }
    int triangale(int a,int b){
        return (a*b)/0.5;
    }
    int circal(int a){
        return 3.14*a*a;
    }
    int show(){
        cout<<endl<<"area of rectangak:"<<rectangal(a,b)<<endl;
        cout<<"area of triangale:"<<triangale(a,b)<<endl;
        cout<<"area of circal:"<<circal(a)<<endl;
    }
};
int main(){
    calculat c;
    c.dete();
    c.show();
}