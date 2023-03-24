//https://www.codingame.com/training/easy/unit-fractions
//UNIT FRACTIONS
#include <bits/stdc++.h>
using namespace std;
#define LL long long int
int main()
{
    LL n;
    cin>>n;
    for(LL i=n+1;i<=2*n;i++){
       LL L=lcm(i,n);
       LL delta=L/n-L/i;
       double y=double(L)/delta;
       if(long(y)==y){
            cout<<fixed<<"1/"<<n<<" = 1/"<<long(y)<<" + 1/"<<long(i)<<endl;
       }
    }
}
