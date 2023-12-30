// Date: 12/03/2023
// This program implements a simple population growth model, where the user inputs the number of years, and it calculates and displays the population for each year based on a growth formula.

#include <iostream>
using namespace std;

int main(){
    int year;
    float pop = 325.7;
    int cYear = 2017;
    cout << "Please enter the number of years: ";
    cin >> year;
    for (int i = 0; i < year; i++)
    {
        cout << "Year " << cYear << "   " << pop << endl;
        pop = pop + ((12.4/1000)* pop) - ((8.4/1000) * pop);
        cYear++;
    }

}