// Write a C++ Program display Student Mark sheet using Multiple inheritance 
#include<iostream>
using namespace std;

class student{
    public:
    string name;
    int roll;

    public:
    void deta(){
        cout<<"enter name:";
        cin.ignore();
        getline(cin,name);
        cout<<"enter roll:";
        cin>>roll;
    }
};
class sheet {
    public:
    int m,e,s,c,res;
    void sub(){
        cout<<endl<<"-----enter marks-------"<<endl;
        cout<<"math:";
        cin>>m;
        cout<<"english:";
        cin>>e;
        cout<<"sci:";
        cin>>s;
        cout<<"computer:";
        cin>>c;

        res=m+e+s+c;
    }
};
class mark : public student , public sheet{
    
    public:
    void show(){
        cout<<endl<<"------Student Mark sheet------"<<endl;
        cout<<"name"<<name<<endl;
        cout<<"roll number:"<<roll<<endl;
        cout<<endl<<"math:"<<m<<endl;
        cout<<"english:"<<e<<endl;
        cout<<"sci:"<<s<<endl;
        cout<<"computer:"<<c<<endl;
        cout<<endl<<"total marks:"<<res<<endl;     
    }
};
int main(){
    mark m;
    m.deta();
    m.sub();
    m.show();
}
