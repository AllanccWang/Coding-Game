//https://www.codingame.com/ide/puzzle/lumen
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;
int n,l;

bool map[25][25];
void lightUPUP(int a,int b){
    int f=l-1;
    for(int i=-f;i<=f;i++){
        for(int j=-f;j<=f;j++){
            if(a+i>=0 && a+i<n && b+j>=0 && b+j<n)
                map[a+i][b+j]=true;
        }
    }
}

int main()
{
    cin >> n; cin.ignore();
    cin >> l; cin.ignore();

    memset(map,false,sizeof(map));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            string cell;
            cin>>cell; cin.ignore();
            if(cell=="C")
                lightUPUP(i,j);
        }
    }
    int cnt=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
            if(!map[i][j]) cnt++;
    }
    cout<<cnt;
}
