//https://www.codingame.com/training/medium/goldbachs-conjecture
//GOLDBACH’S CONJECTURE
#include <bits/stdc++.h>
using namespace std;

int main()
{
    bool p[1000000];
    vector<int> P;
    fill(p,p+1000000,true);
    p[0]=p[1]=false;
    for(int i=1;i<500000;i++) p[2*i]=false;
    for(int i=3;i<1000000;i+=2){
        if(p[i]){
            if(i<500000) P.push_back(i);
            for(int j=2;j*i<1000000;j++) p[i*j]=false;
        }
    }
    int n;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int m;
        int cnt=0;
        cin >> m; cin.ignore();
        if(m==4)
            cnt+=1;
        for(int j=3;j<=m/2;j++){
            if(p[j] && p[m-j])
                cnt+=1;
        }
        cout << cnt << endl;
    }
}
