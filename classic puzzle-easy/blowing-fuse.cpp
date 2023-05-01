//https://www.codingame.com/training/easy/blowing-fuse
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    int m;
    int c;
    cin>>n>>m>>c;
    bool status[100]={false};
    int cc[100]={0};
    memset(status,false,n);
    for(int i=0;i<n;i++) cin>>cc[i];
    int current=0;
    int maxi_current=0;
    for (int i=0;i<m;i++){
        int mx;
        cin>>mx;
        mx-=1;
        if(!status[mx]){
            current+=cc[mx];
            if(current>c){
                cout<<"Fuse was blown."<<endl;
                exit(0);
            }
            status[mx]=!status[mx];
            if(current>maxi_current)
                maxi_current=current;
        }else{
            status[mx]=!status[mx];
            current-=cc[mx];
        }
    }

    cout << "Fuse was not blown." << endl;
    cout << "Maximal consumed current was "<<maxi_current<<" A." << endl;
}
