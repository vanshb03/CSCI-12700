// Date: 12/03/2023
// This program implements a simple binary representation converter, taking an integer input 'n' and outputting its binary representation with a sign bit using the two's complement method.

#include <iostream>
using namespace std;


int main(){
    int n;
    int x;
    int b = 16;
    cin >> n;
    if (n < 0){
        cout << 1;
        x = 32 + n;
    }
    else{
        cout << 0;
        x = n;
    }
    while (b > .5){
        if (x >= b){
            cout << 1;
        }
        else{
            cout << 0;
        }
        x = x % b;
        b = b/2;
    }
    cout << "\n";
}