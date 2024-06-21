//  Write a C++ program to create a class called Car that has private 
// member variables for company, model, and year. Implement member 
// functions to get and set these variables.

#include<iostream>
using namespace std;

class car{

    public:
    string compny,model;
    int year;

    public:

    int getdeta(){

        cout<<"company:";
        cin>>compny;
        cout<<"model:";
        cin>>model;
        cout<<"year:";
        cin>>year;
    }
    int setdeta(){
        cout<<endl<<"company:"<<compny<<endl;
        cout<<"company:"<<model<<endl;
        cout<<"company:"<<year<<endl;
    }

};
int main(){
    car c;
    c.getdeta();
    c.setdeta();
}
