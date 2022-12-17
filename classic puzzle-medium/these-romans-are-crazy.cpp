//https://www.codingame.com/training/medium/these-romans-are-crazy!
//THESE ROMANS ARE CRAZY!
#include <bits/stdc++.h>
using namespace std;
unordered_map<char, int> c = {{'I', 1},{'V', 5},{'X', 10},{'L', 50},{'C', 100},{'D',500},{'M',1000}};
int romanToInt(string s) {
    int result = 0;
    for(int i=0;i<s.size();i++){
        if(i==0||c[s[i]] <= c[s[i - 1]]) 
            result += c[s[i]];
        else
            result += c[s[i]]-2*c[s[i-1]];
    }
    return result;
}
string inttoRoman(int num){
    string str_romans[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string roman = "";
    for (auto i=0;i<13;++i){
        while(num>=values[i]){
            roman += str_romans[i];
            num -= values[i];
        }
    }
    return roman;
}
int main()
{
    string rom1;
    cin >> rom1; cin.ignore();
    string rom2;
    cin >> rom2; cin.ignore();
    int num=romanToInt(rom1)+romanToInt(rom2);
    cout<<inttoRoman(num)<<endl;
}
