// Write a C++ program to implement a class called Employee that has 
// private member variables for name, employee ID, and salary. Include 
// member functions to calculate and set salary based on employee 
// performance. Using of constructor 
#include<iostream>
using namespace std;

class employe{
    private:
    string name;
    int id,salary,r,up;

    public:
     void setdata(){
        cout<<"--------enter employe details---------"<<endl;
        cout<<endl<<"name:";
        cin>>name;
        cout<<"id:";
        cin>>id;
        cout<<"salary:";
        cin>>salary;
        cout<<"enter rating (0-9):";
        cin>>r;

        if(r>=0 && r<=9){
            up=r*salary;
        }
    }
     
     void showdata(){
        cout<<endl<<"name:"<<name<<endl;
        cout<<"id:"<<id<<endl;
        cout<<"salary:"<<salary<<endl;
        cout<<"employe perfomance rating:"<<r<<endl;
        cout<<"update salary"<<up<<endl;
    }

};
int main(){
    employe s;
    s.setdata();
    s.showdata();

   
}