//  Write a program to swap the two numbers using friend function 
// without using third variable 
#include<iostream>
using namespace std;
class swape{
    private:
    int a,b;
    public:
    void data(){
        cout<<"enter num1:";
        cin>>a;
        cout<<"enter num2:";
        cin>>b;
    }
    void show(){
        cout<<endl<<"num1:"<<a<<endl;
        cout<<"num2:"<<b<<endl;
    }
friend void swdata(swape&s);
};
void swdata(swape&s){
    int temp;
    temp=s.a;
    s.a=s.b;
    s.b=temp;
}
int main(){
    swape s;
    s.data();
    cout<<endl<<"befor swap"<<endl;
    s.show();
    swdata(s);
    cout<<endl<<"after swap"<<endl;
    s.show();
}