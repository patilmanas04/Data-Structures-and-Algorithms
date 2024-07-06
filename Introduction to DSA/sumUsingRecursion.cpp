#include <iostream>
using namespace std;

int sum(int n){
    if(n==0) return 0;
    else if(n==1) return 1;
    else return n+sum(n-1);
}

int main(){
    int n;
    cout<<"Enter a number: ";
    cin>>n;

    int totalSum = sum(n);
    cout<<"The sum of all the number till "<<n<<" is: "<<totalSum;

    return 0;
}