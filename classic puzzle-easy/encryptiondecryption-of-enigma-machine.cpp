//https://www.codingame.com/ide/puzzle/encryptiondecryption-of-enigma-machine
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
    string op;
    getline(cin, op);
    int shift;
    cin >> shift; cin.ignore();
    string rotor[4]={"ABCDEFGHIJKLMNOPQRSTUVWXYZ"};
    for (int i = 1; i < 4; i++) {
        getline(cin,rotor[i]);
    }
    string mes;
    getline(cin, mes);
    //Encode part
    if(op.compare("ENCODE")==0){
        for(int i=0;i<mes.size();i++){
            mes[i]=(mes[i]+(i+shift)-'A')%26+'A';
        }
        for (int j = 0; j < 3; j++) {
            string e1="";
            
            for(int i=0;i<mes.size();i++){
                int index=rotor[0].find(mes[i]);
                
                e1+=rotor[j+1][index];
            }
            mes="";
            for(int i=0;i<e1.size();i++)
                mes+=e1[i];
        }
        cout<<mes;
    }
    //Decode part
    else{
        for (int j = 3; j >= 1; j--) {
            string e1="";
            for(int i=0;i<mes.size();i++){
                int index=rotor[j].find(mes[i]);           
                e1+=rotor[0][index];
            }
            mes="";
            for(int i=0;i<e1.size();i++)
                mes+=e1[i];
        }
        //cout<<mes<<endl;
        for(int i=0;i<mes.size();i++){
            mes[i]=(mes[i]-(i+shift)+'A')%26+'A';
        }
        cout<<mes;
    }
}
