//https://www.codingame.com/training/medium/ways-to-make-change
//WAYS TO MAKE CHANGE
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n; cin.ignore();
    int s;
    cin >> s; cin.ignore();
    int a[11]={0};
    for (int i = 0; i < s; i++) {
        cin >> a[i];
    }
    int table[n+1];
    memset(table,0,sizeof(table));
    table[0]=1;
    for(int i=0;i<s;i++){
        for(int j=a[i];j<=n;j++)
            table[j]+=table[j-a[i]];
    }
    cout << table[n] << endl;
}
