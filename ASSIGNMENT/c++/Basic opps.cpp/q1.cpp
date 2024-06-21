 //WAP to create simple calculator using class

 #include<iostream>
 using  namespace std;

 class calculator {

    int a, b;
    public:

    int result(){
        cout<<"\nenter first number:";
        cin>> a;
        cout<<"enter second number:";
        cin>> b;
    }

    int add(){
        return a + b;
    }
    int sub(){
        return a - b;
    }
    int mul(){
        return a * b;
    }
    int div(){
        if(b==0){
            cout<<"division by zero";
        }
        else{
        return a / b;
        }
    }

 };


 int main(){

    int choice;
    char op;
    calculator c;

    cout<<"---------------------manu-----------------------";
    cout<<"\n1.additon"<<endl;
    cout<<"2.subtracton"<<endl;
    cout<<"3.multipication"<<endl;
    cout<<"4.division"<<endl;

    do{

        cout<<"\nenter your choice:";
        cin>> choice;

        switch(choice){

            case 1: c.result();
                    cout<<"result:"<<c.add()<<endl;
                    break;
            case 2: c.result();
                    cout<<"result:"<<c.sub()<<endl;    
                    break;
            case 3: c.result();
                    cout<<"result:"<<c.mul()<<endl;
                    break;
            case 4: c.result();
                    cout<<"result:"<<c.div()<<endl;
                    break;
            default:cout<<"Invalid choice! Please enter a number between 1 and 4."<<endl;
        }
           
            cout<<"------------------------------------------------------------"<<endl;


            cout<<"\ndo you want to perform another calculation? (y/n):";
            cin>> op;
    
    }while(op=='y'||op=='Y');

    cout<<"\n-----------------------thank you--------------------------"<<endl;
    
  
 }




