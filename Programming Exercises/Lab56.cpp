// Name: Vansh Bataviya
// Date: November 2023
// Email: vansh.bataviya94@myhunter.cuny.edu
// Defining Main function that will print Hello World.

#include <iostream>
using namespace std;

int main(){
    int trisize;
    cin >> trisize;
    for (int i = 1; i <= trisize; i++)
    {
        string star(i, '*');
        cout << star << endl;
    }
}
