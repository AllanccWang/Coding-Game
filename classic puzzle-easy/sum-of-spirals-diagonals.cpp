//https://www.codingame.com/training/easy/sum-of-spirals-diagonals
//sum-of-spirals-diagonals
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long int shellcalc(long long int n,long long int s){
    if(n==1)
        return s;
    else if(n==0)
        return 0;
    else
    {
        long long int sum=4*s+(n-1)*6;
        long long int snew=s+4*(n-1);
        long long int nnew=n-2;
        return sum+shellcalc(nnew,snew);
    }
}

int main()
{
    long long int n;
    cin >> n; cin.ignore();
    cout << shellcalc(n,1) << endl;
}
