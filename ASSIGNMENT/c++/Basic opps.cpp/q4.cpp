// Write a C++ program to create a class called Rectangle that has private 
// member variables for length and width. Implement member functions to 
// calculate the rectangle's area and perimeter. 

#include<iostream>
using namespace std;

class rectangal{

    private:
    int width,length;

    public:
    int getdata(){
        cout<<endl<<"enter a length:";
        cin>>length;
        cout<<endl<<"enter a width:";
        cin>>width;
    }
    int area(){
        return length*width;
    }
    int perimeter(){
        return (2*(length+width));
    }


};
int main(){

    rectangal r;
    r.getdata();
    cout<<endl<<"area:"<<r.area();
    cout<<endl<<"perimeter:"<<r.perimeter();
}