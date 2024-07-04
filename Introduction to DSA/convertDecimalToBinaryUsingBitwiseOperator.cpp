#include <iostream>
using namespace std;

string toBinary(int decimanlNumber){
    string binaryNumber = "";
    while(decimanlNumber!=0){
        binaryNumber = to_string(decimanlNumber&1) + binaryNumber;
        decimanlNumber = decimanlNumber>>1;
    }
    return binaryNumber;
}

int main(){
    int decimalNumber;
    cout<<"Enter a decimal number: ";
    cin>>decimalNumber;

    string binaryNumber = toBinary(decimalNumber);
    cout<<"The binary number for "<<decimalNumber<<" is: "<<binaryNumber;

    return 0;
}