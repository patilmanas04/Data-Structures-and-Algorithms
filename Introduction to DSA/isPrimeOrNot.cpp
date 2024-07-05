#include <iostream>
using namespace std;

bool isPrime(int n){
    int noOfFactors = 0;
    for(int i=2 ; i<=n/2 ; i++){
        if(n%i==0) return false;   
    }
    return true;
}

int main(){
    int n;
    cout<<"Enter a number: ";
    cin>>n;

    if(isPrime(n)){
        cout<<"It is a prime number."<<endl;
    }
    else{
        cout<<"It is a composite number."<<endl;
    }

    return 0;
}