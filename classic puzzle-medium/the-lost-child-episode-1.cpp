//https://www.codingame.com/training/medium/the-lost-child-episode-1
//THE LOST CHILD.EPISODE-1
#include <bits/stdc++.h>

using namespace std;
string grid[11];
int shortPath(int mx,int my){
    int m=10,n=10;
    queue<vector<int>> q;
    q.push({mx,my,1});
    bool visit[10][10];
    memset(visit,false,sizeof(visit));
    int dir[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
    int x,y,nxt_x,nxt_y,step;
    while(!q.empty()){
        x=q.front()[0];
        y=q.front()[1];
        step=q.front()[2];
        q.pop();
        if(grid[x][y]=='C') return step;
        for(auto d:dir){
            nxt_x=x+d[0];
            nxt_y=y+d[1];
            if(nxt_x>=0 && nxt_x<10 && nxt_y>=0 && nxt_y<10 && !visit[nxt_x][nxt_y]){
                if(grid[nxt_x][nxt_y]!='#'){
                    q.push({nxt_x,nxt_y,step+1});
                    visit[nxt_x][nxt_y]=true;
                }
            }
        }
    }
    return -1;
}
int main()
{
    int mx=0,my=0;
    for (int i=0;i<10;i++){
        string row;
        getline(cin,row);
        grid[i]=row;
        for(int j=0;j<10;j++)
            if(row[j]=='M'){
                mx=i,my=j;
            }
    }
    int step=shortPath(mx,my)-1;
    cout<<step*10<<"km"<<endl;
}
