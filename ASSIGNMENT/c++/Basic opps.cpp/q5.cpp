// Write a C++ program to create a class called Person that has private 
// member variables for name, age and country. Implement member 
// functions to set and get the values of these variables. 

#include<iostream>
using namespace std;

class person{
    int age;
    string name, contry;
   

    public:
    
    void setdata(){
        cout<<"enter name:";
        cin>>name;
        cout<<"enter age:";
        cin>>age;
        cout<<"enter contry:";
        cin>>contry;
    }
    void getdata(){
        cout<<endl<<"--------------person details------------------";
        cout<<endl<<"person name:"<<name<<endl;
        cout<<"person age:"<<age<<endl;
        cout<<"person contry:"<<contry<<endl;
        
        
    }


};
int main(){
    person p;
    p.setdata();
    p.getdata();
}