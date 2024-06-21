//  Write a C++ program to create a class called Triangle that has private 
// member variables for the lengths of its three sides. Implement member 
// functions to determine if the triangle is equilateral, isosceles, or scalene. 

#include<iostream>
using namespace std;

class triangal{
    private:
    int a,b,c;

    public:
    
    int data(int a, int b, int c){
        if((a==b)&&(b==c)){
            cout<<endl<<"equilanteral triangal"<<endl;
        }
        else if((a==b)||(b==c)||(a==c)){
            cout<<endl<<"isosceles triangal"<<endl;
        }
        else{
            cout<<endl<<"scalene triangal"<<endl;

        }
    }

};
int main(){
   
    int x,y,z;
        cout<<"enter 3 side"<<endl;
        cout<<endl<<"side 1:";
        cin>>x;
        cout<<"side 2:";
        cin>>y;
        cout<<"side 3:";
        cin>>z;
        triangal t;
        t.data(x,y,z);   

    
}