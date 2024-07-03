#include <iostream>
using namespace std;

string convertDecimalToBinary(int decimalNumber){
    string binaryNumber = "";
    while(decimalNumber!=0){
        int remainder = decimalNumber%2;
        binaryNumber = to_string(remainder) + binaryNumber;
        decimalNumber = decimalNumber/2;
    }
    return binaryNumber;
}

int main(){
    int decimalNumber;
    cout<<"Enter the decimal number: ";
    cin>>decimalNumber;

    if(decimalNumber!=0 && decimalNumber>0){
        string binaryNumber = convertDecimalToBinary(decimalNumber);
        cout<<"The Binary Number for "<<decimalNumber<<" is "<<binaryNumber<<endl;
    }
    else if(decimalNumber==0){
        cout<<"The Binary Number for "<<decimalNumber<<" is 0"<<endl;
    }
    else{
        cout<<"Enter a valid input"<<endl;
    }

    return 0;
}