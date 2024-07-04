#include <iostream>
using namespace std;

int main(){
    int n1, n2;
    cout<<"Enter first number: ";
    cin>>n1;
    cout<<"Enter second number: ";
    cin>>n2;

    cout<<"Bitwise AND (&) -> "<<n1<<" & "<<n2<<": "<<(n1&n2)<<endl;
    cout<<"Bitwise OR (|) -> "<<n1<<" & "<<n2<<": "<<(n1|n2)<<endl;
    cout<<"Bitwise NOT (~) -> "<<n1<<" & "<<n2<<": "<<(~n1)<<endl;
    cout<<"Bitwise XOR (^) -> "<<n1<<" & "<<n2<<": "<<(n1^n2)<<endl;

    return 0;
}