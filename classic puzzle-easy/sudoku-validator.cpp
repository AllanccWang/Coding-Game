//https://www.codingame.com/ide/puzzle/sudoku-validator
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define N 9

int map[9][9];
using namespace std;
//check whether num is present in col or not
bool isPresentInCol(int col, int num){
   for (int row = 0; row < N; row++)
      if (map[row][col] == num)
         return true;
   return false;
}
//check whether num is present in row or not
bool isPresentInRow(int row, int num){
   for (int col = 0; col < N; col++)
      if (map[row][col] == num)
         return true;
   return false;
}
//check whether num is present in 3x3 box or not
bool isPresentInBox(int boxStartRow, int boxStartCol, int num){
   for (int row = 0; row < 3; row++)
      for (int col = 0; col < 3; col++)
         if (map[row+boxStartRow][col+boxStartCol] == num)
            return true;
   return false;
}

int main()
{
    map[9][9]={0};
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cin>>map[i][j];
        }
    }
    for (int i = 0; i < 9; i++)
        for (int j=1;j<=9;j++)
            if (!isPresentInCol(i,j)){
                cout<<"false";
                exit(0);
            }
    for (int i = 0; i < 9; i++)
        for (int j=1;j<=9;j++)
            if (!isPresentInRow(i,j)){
                cout<<"false";
                exit(0);
            }
    for (int i = 0; i < 9; i+=3)
        for (int k = 0; k < 9; k+=3)
            for (int j=1;j<=9;j++)
                if (!isPresentInBox(i,k,j)){
                    cout<<"false";
                    exit(0);
            }
    cout<<"true";
}
