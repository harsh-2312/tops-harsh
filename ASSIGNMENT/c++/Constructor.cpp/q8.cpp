// Write a C++ program to implement a class called Student that has private 
// member variables for name, class, roll number, and marks. Include 
// member functions to calculate the grade based on the marks and display 
// the student's information. Accept address from each student implement 
// using of aggregation 

#include<iostream>
using namespace std;

class student{
    private:
    string name;
    int cla,mark,roll;

    public:
    int setdata(){
        cout<<"------student detail------"<<endl;
        cout<<endl<<"enter name:";
        cin>>name;
        cout<<"enter class:";
        cin>>cla;
        cout<<"enter roll number:";
        cin>>roll;
        cout<<"enter mark:";
        cin>>mark;
    }
    char graddata(){    
        if(mark>=90){
            return 'A';
        }
        else if(mark>=80){
            return 'B';
        }
        else if(mark>=70){
            return 'C';
        }
        else if(mark>=60){
            return 'D';
        }
        else if(mark>=50){
            return 'E';
        }
        else{
            return 'F';
        }
    }
    int showdata(){
        cout<<endl<<"name:"<<name<<endl;
        cout<<"class:"<<cla<<endl;
        cout<<"roll number:"<<roll<<endl;
        cout<<"mark:"<<mark<<endl;
        cout<<"grade:"<<graddata()<<endl;
    }

};
int main(){
    student s;
    s.setdata();
    s.showdata();

}