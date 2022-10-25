//https://www.codingame.com/training/easy/reverse-minesweeper
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
string map[30];
int cnt[30][30];
int w,h;
void mineCounter(int r,int c){
    for(int i=-1;i<=1;i++)
        for(int j=-1;j<=1;j++){
            if(r+i>=0 && r+i<h && c+j>=0 && c+j<w && map[r+i][c+j]!='x')
                cnt[r+i][c+j]+=1;
        }
}
int main()
{
    cin >> w; cin.ignore();
    cin >> h; cin.ignore();
    for (int i = 0; i < h; i++) {
        getline(cin,map[i]);
    }
    for(int i=0;i<h;i++)
        for(int j=0;j<w;j++)
            if(map[i][j]=='x'){
                mineCounter(i,j);
            }
    for(int i=0;i<h;i++)
        for(int j=0;j<w;j++)
            if(map[i][j]=='x'){
                map[i][j]='.';
            }
    for(int i=0;i<h;i++){
        for(int j=0;j<w;j++){
            if(cnt[i][j]!=0)
                cout<<cnt[i][j];
            else
                cout<<map[i][j];
        }
        cout<<endl;
    }
}
