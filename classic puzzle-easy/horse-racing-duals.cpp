//https://www.codingame.com/training/easy/horse-racing-duals
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
    int arr[100001]={0};
    int ln=0;
    int n;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int pi;
        cin >> pi; cin.ignore();
        arr[ln++]=pi;
    }
    int MAX=1e8;
    sort(arr,arr+n);
    for(int i=1;i<n;i++)
        if(abs(arr[i]-arr[i-1])<=MAX)
            MAX=abs(arr[i]-arr[i-1]);
    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << MAX << endl;
}
