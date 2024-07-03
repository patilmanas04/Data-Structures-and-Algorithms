#include <iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter a number: ";
    cin>>n;
    if((n&1)%10==0){
        cout<<"It is an even number"<<endl;
    }
    else{
        cout<<"It is an odd number"<<endl;
    }
    return 0;
}