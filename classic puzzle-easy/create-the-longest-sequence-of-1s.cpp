//https://www.codingame.com/training/easy/create-the-longest-sequence-of-1s
//create-the-longest-sequence-of-1s
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

int main()
{
    string b;
    getline(cin, b);
    int a[1001],ln=b.size(),aln=0;
    for(int i=0;i<ln;i++)
        if(b[i]=='0') a[aln++]=i;
    int max_length=0;
    for(int i=0;i<aln;i++){
        string s="";
        for(int j=0;j<ln;j++)
            if(j==a[i]) s+='1';
            else s+=b[j];
        stringstream ss(s);
        string word;
        while (!ss.eof()){
            getline(ss,word,'0');
            max_length=max((int)word.size(),max_length); 
            //be aware of adding (type) as it indicates in the comment
        }
    }
    cout<<max_length<<endl;
}
