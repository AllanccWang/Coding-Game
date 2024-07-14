//https://www.codingame.com/training/medium/folding-paper
//folding-paper
#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    string order;
    getline(cin, order);
    string side;
    getline(cin, side);
    //record the number of layers for each sides
    map<char,int> folds={{'R',1},{'L',1},{'U',1},{'D',1}};
    for(int i=0;i<order.size();i++){
        //operate the layers for each side depending on the folding direction
        for(auto const &n: folds)
            if(n.first!=order[i]){
                if((order[i]=='R' && n.first=='L') || (order[i]=='L' && n.first=='R') ||
                    (order[i]=='U' && n.first=='D') || (order[i]=='D' && n.first=='U')){
                        folds[n.first]+=folds[order[i]];
                    }
                else
                    folds[n.first]*=2;
            }
        folds[order[i]]=1;
    }
    cout<<folds[side[0]];
}
