// Name: Vansh Bataviya
// Date: November 2023
// Email: vansh.bataviya94@myhunter.cuny.edu
// Defining Main function that will print Hello World.

#include <iostream>
using namespace std;

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