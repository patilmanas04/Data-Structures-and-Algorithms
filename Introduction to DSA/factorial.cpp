#include <iostream>
using namespace std;

int factorialUsingLoop(int n){
    int factorial = 1;
    for(int i=n ; i>0 ; i--){
        factorial*=i;
    }
    return factorial;
}

int factorialUsingRecursion(int n){
    if(n==0 || n==1){
        return 1;
    }
    else{
        return n*factorialUsingRecursion(n-1);
    }
}

int main(){
    int n;
    cout<<"Enter a number to find it's factorial: ";
    cin>>n;

    int factorialLoop = factorialUsingLoop(n);
    cout<<"The factorial of "<<n<<" is: "<<factorialLoop<<endl;

    int factorialRecursion = factorialUsingRecursion(n);
    cout<<"The factorial of "<<n<<" is: "<<factorialRecursion;

    return 0;
}