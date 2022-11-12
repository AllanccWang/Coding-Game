//Spiral matrix algorithm
/*
Input:
turns = 5
1 2 3 4
5 * * 8
9 * * 12
13 14 15 16

Output:
12 16 15 14
8 * * 13
4 * * 9
3 2 1 5
*/
#include <bits/stdc++.h>
#define R 4
#define C 4
using namespace std;

void rotatematrix(int m, int n, int mat[R][C])
{
    int prev, curr;

    prev = mat[1][n-1];
    for (int i = n-1; i>=0; i--){
        curr = mat[0][i];
        mat[0][i] = prev;
        prev = curr;
    }
  
    for (int i = 1; i < m; i++){
        curr = mat[i][0];
        mat[i][0] = prev;
        prev = curr;
    }

    for (int i = 1; i < n-1; i++){
        curr = mat[m-1][i];
        mat[m-1][i] = prev;
        prev = curr;

    }

    for (int i = m-1; i > 0; i--){
        curr = mat[i][n-1];
        mat[i][n-1] = prev;
        prev = curr;
    }
    
}

int main(){
    // Case 1
    int a[R][C] = { {1, 2, 3, 4}, {5, 6, 7, 8},
        {9, 10, 11, 12}, {13, 14, 15, 16} };

    // Print rotated matrix
    for (int i=0; i<R; i++) {
        for (int j=0; j<C; j++)
            if(i<R-1 && i>0 && j>0 && j<C-1)
                cout<<"* ";
            else cout << a[i][j] << " ";
        cout<<endl;
    }
    cout<<"---------------------------------\n";
    cout<<"Counter-clockwise Rotated Matrix:\n";
    int turns=5;
    while(turns--)
        rotatematrix(R, C, a);
        
    // Print rotated matrix
    for (int i=0; i<R; i++) {
        for (int j=0; j<C; j++)
            if(i<R-1 && i>0 && j>0 && j<C-1)
                cout<<"* ";
            else cout << a[i][j] << " ";
        cout<<endl;
    }
    return 0;
}
