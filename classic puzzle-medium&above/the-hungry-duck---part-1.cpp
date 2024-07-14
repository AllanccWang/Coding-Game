//https://www.codingame.com/training/hard/the-hungry-duck---part-1
#include <bits/stdc++.h>
using namespace std;
int grid[11][11];
int sum[11][11];

int main()
{
    int w;
    int h;
    cin>>w>>h; cin.ignore();
    for(int i=0;i<h;i++)
        for(int j=0;j<w;j++){
            int food;
            cin>>food; cin.ignore();
            grid[i][j]=food;
        }
    for(int i=1;i<=h;i++){
        for(int j=1;j<=w;j++){
            sum[i][j]=max(sum[i-1][j],sum[i][j-1])+grid[i-1][j-1];
        }
    }
    cout<<sum[h][w]<<endl;
}
