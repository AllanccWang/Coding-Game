//https://www.codingame.com/training/medium/sandpile-addition
//SANDPILE ADDITION
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;
int m[10][10];
//check the grains per pile
bool check_grains(int m[][10],int n){
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            if(m[i][j]>3) return true;
    return false;
}
int main()
{
    int n;
    cin >> n; cin.ignore();
    memset(m,0,sizeof(n*n));
    string row;
    for (int i = 0; i < n; i++) {
        getline(cin, row);
        for(int j=0;j<row.size();j++)
            m[i][j]=row[j]-'0';
    }
    for (int i = 0; i < n; i++) {
        getline(cin, row);
        for(int j=0;j<row.size();j++){
            m[i][j]+=row[j]-'0';
        }
    }
    
    while(check_grains(m,n)){
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                if(m[i][j]>3)
                {
                    //add the grains to neighbors
                    int g=m[i][j]/4;
                    m[i][j]%=4;
                    if(i+1<n) m[i+1][j]+=g;
                    if(j+1<n) m[i][j+1]+=g;
                    if(i-1>=0) m[i-1][j]+=g;
                    if(j-1>=0) m[i][j-1]+=g;
                }
            }
        
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
            cout<<m[i][j];
        cout<<endl;
    }
}
