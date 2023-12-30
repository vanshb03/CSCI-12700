// Date: 12/03/2023
// This program implements a simple console application in C++ that prompts the user to enter a year, ensures it is 2018 or earlier through a loop, and then outputs the entered year.

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