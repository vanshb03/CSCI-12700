// Date: 12/03/2023
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
