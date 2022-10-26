//https://www.codingame.com/ide/puzzle/temperatures
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int n; // the number of temperatures to analyse
    int close=5527;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int t; // a temperature expressed as an integer ranging from -273 to 5526
        cin >> t; cin.ignore();
        if(abs(t)<abs(close)){
            close=t;
        }else if(abs(t)==abs(close) && t>0)
            close=t;
            
    }

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;
    if(close==5527)
        cout<<0<<endl;
    else
        cout << close << endl;
}
