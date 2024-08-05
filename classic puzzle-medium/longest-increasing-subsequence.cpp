//https://www.codingame.com/training/medium/longest-increasing-subsequence
//LONGEST INCREASING SUBSEQUENCE
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n; cin.ignore();
    int arr[2570];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    int m[2570]={0};
    for(int i=0;i<n;i++) m[i]=1;

    for(int i=0;i<n;i++){
        for(int j=i;j<n;j++){
            if(arr[j]>arr[i] && m[j]<m[i]+1)
                m[j]=m[i]+1;
        }
    }

    cout <<*max_element(m,m+n)<< endl;
}
