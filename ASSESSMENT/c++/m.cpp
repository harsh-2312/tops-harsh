// Create a lecture management System  

// Data members: 
// a) Name of the lecturer 
// b) Name of the subject 
// c) Name of course 
// d) Number of lecturers 
// Data functions:  
// a) To assign initial values  
// b) To add a lecture details  
// c) To display name and lecture details 

#include<iostream>
using namespace std;

class management{
    public:
    string lecturer,subject,course;
    int lecturers;
    public:
    void assign(string lec, string sub, string cou, int num){
        lecturer=lec;
        subject=sub;
        course=cou;
        lecturers=num;
    }
    void getdata(){
        cout<<"enter lecturer name:";
        cin>>lecturer;
        cout<<"enter subject name:";
        cin>>subject;
        cout<<"enter course name:";
        cin>>course;
        cout<<"enter Number of lecturers:";
        cin>>lecturers;
    }
    void show(){
        cout<<"Name of the lecturer:"<<lecturer<<endl;
        cout<<"Name of the subject:"<<lecturer<<endl;
        cout<<"Name of the course:"<<lecturer<<endl;
        cout<<"Name of the lecturers:"<<lecturer<<endl;
    }
};
int main(){
    management m[5];
    for(int i=0;i<5;i++){
        cout<<endl<<"enter details of lecturer:"<<(i+1)<<endl;
        m[i].getdata();
    }
    cout<<endl<<"-----------------------------------------------------"<<endl;
    for(int i=0;i<5;i++){
        cout<<endl<<"details of lecturer:"<<(i+1)<<endl;
        m[i].show();
    }
}
