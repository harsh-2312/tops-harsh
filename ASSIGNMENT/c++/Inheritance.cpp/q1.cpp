// Assume a class cricketer is declared. Declare a derived class batsman from 
// cricketer. Data member of batsman. Total runs, Average runs and best 
// performance. Member functions input data, calculate average runs, Display 
// data. (Single Inheritance) 

#include<iostream>
using namespace std;

class cricketer{
    public:
    string name;
    int age,run,avrun,pr,match=5;

    public:
    int getdeta(){

        cout<<"enter name:";
        cin>>name;
        cout<<"enter age:";
        cin>>age;
    }
};
class batsman : public cricketer{
    
    public:

    int set(){
        cout<<"enter total run:";
        cin>>run;
        avrun=run/match;

        cout<<endl<<"name:"<<name<<endl;
        cout<<"age:"<<age<<endl;
        cout<<"total run:"<<run<<endl;
        cout<<"total match:"<<match<<endl;
        cout<<"avreage run:"<<avrun<<endl;
        cout<<"batsman performance:"<<endl;
        if(avrun>=80){
            cout<<endl<<"best player\n";
        }
        else if(avrun>=40){
            cout<<endl<<"avreage player\n";
        }
        else{
            cout<<endl<<"bed player\n";
        }
    }  
};
int main(){
    batsman b;
    b.getdeta();
    b.set();
}
