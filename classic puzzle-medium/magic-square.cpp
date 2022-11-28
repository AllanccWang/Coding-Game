//https://www.codingame.com/training/medium/magic-square
//magic-square
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;
int map[100][100];
int a[100];
bool check_in_array(int n){
    for(int i=0;i<n*n;i++)
        if(a[i]!=0) return false;
    return true;
}
int main()
{
    int n;
    cin >> n; cin.ignore();
    memset(map,0,sizeof(map));
    memset(a,0,sizeof(a));
    for(int i=1;i<=n*n;i++) a[i-1]=i;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int c;
            cin >> c; cin.ignore();
            map[i][j]=c;
            a[c-1]=0; // check 1,2,...n*n is distinct and in array
        }
    }
    if(!check_in_array(n)){
        cout<<"MUGGLE\n";exit(0);
    }else
    {
        bool flag=true;
        int num=0,s=0;
        //check sum per row
        for(int i=0;i<n;i++)
            num+=map[0][i];
        for(int i=0;i<n;i++){
            s=0;
            for(int j=0;j<n;j++)
                s+=map[i][j];
            if(s!=num){
                flag=false;
                break;
            }
        }
        //check sum per col
        for(int i=0;i<n;i++){
            s=0;
            for(int j=0;j<n;j++)
                s+=map[j][i];
            if(s!=num){
                flag=false;
                break;
            }
        }
        //check diagonal sum
        s=0;
        for(int i=0;i<n;i++)
            s+=map[i][i];
        if(s!=num) flag=false;
        s=0;
        for(int i=0;i<n;i++)
            s+=map[i][n-i-1];            
        if(s!=num) flag=false;

        if(flag) cout<<"MAGIC\n";
        else cout<<"MUGGLE\n";
    }
}
