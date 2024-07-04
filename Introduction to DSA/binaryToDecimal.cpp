#include <iostream>
#include <math.h>
using namespace std;

int toDecimal(int binaryNumber){
    int decimalNumber = 0;
    int index = 0;
    while(binaryNumber!=0){
        if(binaryNumber%10==1){
            decimalNumber += (int)pow(2, index);
        }
        binaryNumber = (int)binaryNumber/10;
        index++;
    }
    return decimalNumber;
}

int main(){
    int binaryNumber;
    cout<<"Enter a binary number: ";
    cin>>binaryNumber;

    int decimalNumber = toDecimal(binaryNumber);
    cout<<"The decimal number for "<<binaryNumber<<" is: "<<decimalNumber;

    return 0;
}