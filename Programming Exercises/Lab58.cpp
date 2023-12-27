// Name: Vansh Bataviya
// Date: November 2023
// Email: vansh.bataviya94@myhunter.cuny.edu
// Defining Main function that will print Hello World.

#include <iostream>
using namespace std;

int main(){
    int year;
    cout << "Enter year: ";
    cin >> year;
    while (year > 2018){
        cout << "Year must be 2018 or earlier: ";
        cin >> year;
    }
    cout << "You entered: " << year;
}