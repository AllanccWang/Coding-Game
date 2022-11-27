//https://www.codingame.com/training/medium/rubik%C2%AE
//RUBIK®
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n; cin.ignore();
    long ans=n*n*2+(n*2+2*(n-2))*(n-2);
    if(n==1) ans=1;
    cout << ans << endl;
}
