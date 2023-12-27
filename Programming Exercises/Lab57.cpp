// Name: Vansh Bataviya
// Date: November 2023
// Email: vansh.bataviya94@myhunter.cuny.edu
// Defining Main function that will print Hello World.

#include <iostream>
using namespace std;

#include <iostream>
using namespace std;

int main(){
    cout << "Enter month (as a number): ";
    int month;
    cin >> month;
    if (month < 3 or month > 11){
        cout << "Happy Winter";
    }
    else if (month >= 3 and month < 7){
        cout << "Happy Spring";
    }
    else if (month >= 7 and month < 9){
        cout << "Happy Summer";
    }
    else{
        cout << "Happy Fall";
    }
}
