// Write a C++ Program to find Area of Rectangle using inheritance
#include<iostream>
using namespace std;

class shape{
    public:
    int l,w,res;
    
    int setdata(){
    cout<<"enter length:";
    cin>>l;
    cout<<"enter wilth:";
    cin>>w;

    // res=l*w;
   // cout<<endl<<"Area of Rectangle"<<res<<endl;
    }   
};
class rectangal : public shape{

    public:
    int getdata(){
        res=l*w;
        cout<<endl<<"Area of Rectangle"<<res<<endl;
     
    }

   
};
int main(){
    rectangal r;
    r.setdata();
    r.getdata();
   
}






































//     public:
//     int l,w;
//     int setdata(int l,int w){
//         cout<<"enter langth:";
//         cin>>l;
//         cout<<"enter wilth:";
//         cin>>w;
//     }
// };
// class rectangle : public shape{

//     int get(int l,int w){
//         return l*w;
//     }
// }; 
// int main(){
//     int l,w;
//    rectangle r;
//    r.setdata(l,w);
//   // r.get();
//    cout<<"Area of Rectangle:"<<r.get(l,w)<<endl;
// }