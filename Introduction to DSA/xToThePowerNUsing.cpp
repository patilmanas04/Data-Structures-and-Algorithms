#include <iostream>
using namespace std;

int powUsingIterative(int x, int n){
    int result = 1;
    for(int i=1 ; i<=n ; i++){
        result*=x;
    }
    return result;
}

int powUsingRecursion(int x, int n){
    if(n==1){
        return x;
    }
    else{
        return x*powUsingRecursion(x, n-1);
    }
}

int main(){
    int x, n;
    cout<<"Enter the number(x): ";
    cin>>x;
    cout<<"Enter the power to the x(n): ";
    cin>>n;

    int resultUsingIterative = powUsingIterative(x, n);
    cout<<x<<"^"<<n<<" using iterative approach: "<<resultUsingIterative<<endl;

    int resultUsingRecursion = powUsingRecursion(x, n);
    cout<<x<<"^"<<n<<" using iterative approach: "<<resultUsingRecursion<<endl;

    return 0;
}