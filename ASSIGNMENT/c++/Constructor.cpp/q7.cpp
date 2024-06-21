// Write a C++ program to implement a class called Date that has private 
// member variables for day, month, and year. Include member functions to 
// set and get these variables, as well as to validate if the date is valid. 

#include<iostream>
using namespace std;

class date{
    private:
    int day,month,year;

    public:
    int setdata(){
        cout<<"enter day:"; 
        cin>>day;
        cout<<"enter month:";
        cin>>month;
        cout<<"enter year:";
        cin>>year;

        if(year<0 || day<1 || day>31 || month<1 || month>12){
            return false;
        }
        if(month==2){
            if((year %4==0 && year %100!=0) || (year %400==0)){
                return day<=29;
            }
                else{
                    return day<=28;
                }
            
        }
        if(month==4 || month==6 || month==8 || month==10 || month==12){
            return day<=30;
        }
        else{
            return day<=31;
        }
    }
};
int main(){

    date d;
    if(d.setdata()){
        cout<<endl<<"date is valid"<<endl;
    }
    else{
        cout<<endl<<"date is not valid"<<endl;
    }

}