// Write a C++ program to implement a class called Bank Account that has 
// private member variables for account number and balance. Include 
// member functions to deposit and withdraw money from the account.

#include<iostream>
using namespace std;

class bank{

    private:
    int num,bal,dp,wi;

    public:
    int data(){
        cout<<"account number:";
        cin>>num;
        cout<<"balance:";
        cin>>bal;
     }
    int deposit(){
        cout<<endl<<"enter deposit amount:";
        cin>>dp;
        bal+=dp;
        cout<<endl<<"after deposit amount is:"<<bal<<endl;

    }
    int withdraw(){
        cout<<endl<<"entenr withdraw amount:";
        cin>>wi;
        bal-=wi;
        cout<<endl<<"after withdraw amount is:"<<bal<<endl;
        
    }


};
int main(){
    bank b;
    b.data();
    b.deposit();
    b.withdraw();
}