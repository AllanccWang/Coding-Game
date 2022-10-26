//https://www.codingame.com/ide/puzzle/merlins-magic-square
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
string map[3],tmp[3];
bool charCheck(){
    int cnt=0;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(map[i][j]=='*')
                cnt++;
        }
    }
    if(cnt==8 && map[1][1]=='~')
        return true;
    else
        return false;
}
void fcharFlip(int i,int j){
    if(map[i][j]=='~')
        map[i][j]='*';
    else 
        map[i][j]='~';
}
void cornerFlip(int n){
    if(n==1)
        fcharFlip(0,0), fcharFlip(0,1), fcharFlip(1,0), fcharFlip(1,1);
    else if(n==3)
        fcharFlip(0,1), fcharFlip(1,1), fcharFlip(0,2), fcharFlip(1,2);
    else if(n==7)
        fcharFlip(1,0), fcharFlip(1,1), fcharFlip(2,0), fcharFlip(2,1);
    else if(n==9)
        fcharFlip(1,1), fcharFlip(2,1), fcharFlip(1,2), fcharFlip(2,2);
}
void bordFlip(int n){
    if(n==2)
        fcharFlip(0,0), fcharFlip(0,1), fcharFlip(0,2);
    else if(n==4)
        fcharFlip(0,0), fcharFlip(1,0), fcharFlip(2,0);
    else if(n==6)
        fcharFlip(0,2), fcharFlip(1,2), fcharFlip(2,2);
    else if(n==8)
        fcharFlip(2,0), fcharFlip(2,1), fcharFlip(2,2);
}
void centerFlip(){
    fcharFlip(0,1), fcharFlip(1,1), fcharFlip(2,1), fcharFlip(1,0), fcharFlip(1,2);
}
void recoverMap(){
    for(int i=0;i<3;i++)
        map[i]=tmp[i];
}
int main()
{
    for(int i=0;i<3;i++){
        string s;
        getline(cin,s);
        for(int j=0;j<s.size();j++){
            if(s[j]!=' ') map[i]+=s[j];
        }
    }

    string press;
    getline(cin, press);
    for(int i=0;i<press.size();i++){
        if(press[i]=='1' | press[i]=='3' | press[i]=='7' | press[i]=='9')
            cornerFlip(press[i]-'0');
        else if(press[i]=='2' | press[i]=='4' | press[i]=='6' | press[i]=='8')
            bordFlip(press[i]-'0');
        else
            centerFlip();
    }
    
    for(int i=0;i<3;i++)
        tmp[i]=map[i];
    
    for(int i=1;i<10;i++){
        if(i%2 && i!=5)
            cornerFlip(i);
        else if(i%2==0)
            bordFlip(i);
        else
            centerFlip();
        if(charCheck()){
            cout<<i;
            break;
        }else{
            recoverMap();
        }
    }

}
