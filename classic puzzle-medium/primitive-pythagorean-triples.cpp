//https://www.codingame.com/training/medium/primitive-pythagorean-triples
//PRIMITIVE PYTHAGOREAN TRIPLES
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int C;
    cin>>C;
    int c=ceil(sqrt(C));
    int cnt=0;
    //https://mathworld.wolfram.com/PythagoreanTriple.html
    for(int m=1;m<c;m++)
        for(int n=m+1;n<c;n++)
            if(gcd(m,n)==1&&(m+n)%2==1&&(m*m+n*n)<=C) cnt++;
    cout<<cnt<<endl;
}
