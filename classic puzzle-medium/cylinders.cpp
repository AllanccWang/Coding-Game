//https://www.codingame.com/training/medium/cylinders
//CYLINDERS
//check if it can be done by permutation method in ruby
#include <bits/stdc++.h>
using namespace std;
double r[11];
double x[11];
double best[11];
double Min=1e9;
//update the center of the number,t circle
double center(int t){
    double length=0;
    for(int i=0;i<t;i++){
        double temp=x[i]+2*sqrt(r[i]*r[t]);
        if(temp>length)
            length=temp;
    }
    return length;
}
//calculate total length of circles
void calculate_length(int N){
    double left=0;
    double right=0;
    for(int i=0;i<N;i++){
        if(x[i]-r[i]<left)
            left=x[i]-r[i];
        if(x[i]+r[i]>right)
            right=x[i]+r[i];
    }
    if(right-left<Min){
        Min=right-left;
        for(int i=0;i<N;i++)
            best[i]=r[i];
    }
}
void dfs(int t,int N){
    if(t==N)
        calculate_length(N);
    else{
        for(int i=t;i<N;i++){
            swap(r[t],r[i]);
            double cen=center(t);
            //new center length updated
            if(r[0]+cen+r[t]<Min){
                x[t]=cen;
                dfs(t+1,N);
            }
            swap(r[t],r[i]);
        }
    }
}
int main()
{
    int cases;
    cin >> cases; cin.ignore();
    for (int i = 0; i < cases; i++) {
        while(!cin.eof()){
            int n;
            cin>>n;
            Min=1e9;
            for(int j=0;j<n;j++)
                cin>>r[j];
            dfs(0,n);
            printf("%.3f\n",Min); 
        }   
    }
}
