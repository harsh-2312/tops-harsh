// Assume that the test results of a batch of students are stored in three different
// classes. Class Students are storing the roll number. Class Test stores the
// marks obtained in two subjects and class result contains the total marks
// obtained in the test. The class result can inherit the details of the marks
// obtained in the test and roll number of students. (Multilevel Inheritance)

#include <iostream>
using namespace std;

class student
{
public:
    string name;
    int roll;

public:
    void data()
    {
        cout << "enter name:";
        cin.ignore();
        getline(cin,name);
        cout << "enter roll number:";
        cin >> roll;
    }
};
class test : public student
{
public:
    int a, b;

public:
    void mark()
    {
        cout << "english:";
        cin >> a;
        cout << "math:";
        cin >> b;
    }
};
class result : public test
{

public:

    void show()
    {
        cout << endl
             << "name:" << name << endl;
        cout << endl
             << "roll number:" << roll << endl;
        cout << endl
             << "english:" << a << endl;
        cout << endl
             << "math:" << b << endl;
        cout << endl
             << "total mark:" << a+b << endl;
    }
};
int main()
{
    result r;
    r.data();
    r.mark();
    r.show();
}