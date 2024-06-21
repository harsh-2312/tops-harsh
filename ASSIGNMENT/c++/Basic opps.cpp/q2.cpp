// Define a class to represent a bank account. Include the following members: 

#include<iostream>
using namespace std;

class accound{

    public:
    string name,ac_type;
    int ac_num,d_amt,curr_amt=50000,bal,w_amt,c=0;

    public:
     int details(){

        cout<<"------------------enter a details--------------------"<<endl;
        cout<<endl<<"Name of the depositor:";
        cin>>name;
        cout<<endl<<"Account number:";
        cin>>ac_num;
        cout<<endl<<"Type of account:";
        cin>>ac_type;
    
        
    }
    int deposit(){

        cout<<endl<<"Enter deposit amount:";
        cin>>d_amt;
        bal=curr_amt+d_amt;
        cout<<endl<<"After deposit amount:"<<bal;
        c+=bal;
    }
    int checkbal(){
        // c+=bal;
        cout<<endl<<"current balance is:"<<c<<endl;
    }
    int withdraw(){

        cout<<endl<<"Enter withdraw amount:";
        cin>>w_amt;
        bal-=w_amt;
        cout<<endl<<"After withdraw amount is:"<<bal;
    }


};
int main(){

    accound ac;
    ac.details();
    int choice;

    // cout<<endl<<"1.deposits"<<endl;
    // cout<<"2.withdraw"<<endl;
    // cout<<"3.chake balance"<<endl;
    // cout<<endl<<"enter yore choice:";
    // cin>>choice;

    // switch(choice){

    //     case 1: 
    //         ac.deposit();
    //         break;
    //     case 2:
    //         ac.withdraw();
    //         break;
    //     case 3:
    //         ac.checkbal();
    //         break;
    //     default : cout<<"Invalid choice!"<<endl;           


    // }


   // ac.details();
    ac.deposit();
    ac.checkbal();
    ac.withdraw();

}