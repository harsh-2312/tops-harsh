// Create a class person having members name and age. Derive a class student 
// having member percentage. Derive another class teacher having member 
// salary. Write necessary member function to initrialize, read and write data. 
// Write also Main function (Multiple Inheritance) 

#include<iostream>
using namespace std;

class person{
protected:
    int age;
    string name;
public:
    void pdata(){
        cout<<"enter name:";
        cin>>name;
        cout<<"enter age:";
        cin>>age;
    }
};
class student : public person{
protected:
    int percentage;
public:
    void mark(){
        cout<<"enter percentage:";
        cin>>percentage;
    }
};
class teacher : public student{
protected:
    int salary;
public:
    void set(){
        cout<<"enter teacher salary:";
        cin>>salary;
    }
    void display(){
        cout<<endl<<"---------------------------------"<<endl;
        cout<<"NAME: "<<name<<endl;
        cout<<"AGE: "<<age<<endl;
        cout<<"PERCENTAAGE: "<<percentage<<"%"<<endl;
        cout<<"SALARY: "<<salary<<endl;
    }

};
int main(){
    teacher t;
    t.pdata();
    t.mark();
    t.set();
    t.display();
}




