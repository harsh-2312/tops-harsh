//9. Write a Program of Two 1D Matrix Addition using Operator Overloading//
#include<iostream>
using namespace std;
class Matrix{
    int a[4];
    public:
    void get_data();
    void display();
    void operator +(Matrix x);
};
void Matrix::get_data(){
    cout<<"\n Enter matrix element : \n";
    for(int i=0;i<4;i++){
        cout<<" ";
        cin>>a[i];
    }
}
void Matrix::display(){
    for(int i=0;i<4;i++){
        cout<<a[i]<<"\t";
    }
}
void Matrix::operator +(Matrix x){
    int mat[4];
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            mat[i]=a[i]+x.a[i];
        }
    }
    cout<<"\n\n Addition of Matrix: \n\n";
    for(int i=0;i<4;i++){
        cout<<mat[i]<<"\t";
    }
    cout<<"\n";
}
int main(){
    Matrix m,n;
    m.get_data();
    n.get_data();
    cout<<"\n First Matrix : \n\n";
    m.display();
    cout<<"\n Second Matrix : \n\n";
    n.display();
    m+n;  //operator overloading
}