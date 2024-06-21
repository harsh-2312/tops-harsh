//Write a C++ program to implement a class called Circle that has private 
//member variables for radius. Include member functions to calculate the 
//circle's area and circumference. 

#include<iostream>
using namespace std;

class circal{
    private:
    float radius;

    public:
    // float setradius(float r){
    //     radius=r;
    // }
    float getdata(){
        cout<<"enter radius of circal:";
        cin>>radius;
    }
    float area(){
        return 3.14*radius*radius;
    }
    float circum(){
        return 2*3.14*radius;
    }
    };
    int main(){
        circal c;
        c.getdata();
        cout<<endl<<"area of circal is:"<<c.area();
        cout<<endl<<"circumference is:"<<c.circum();
    }


