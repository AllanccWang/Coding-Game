//https://www.codingame.com/training/medium/number-of-paths-between-2-points
//NUMBER OF PATHS BETWEEN 2 POINTS
#include <bits/stdc++.h>
using namespace std;
int r,c;
int numberOfPath(int A[][10]){

	if (A[0][0])
		return 0;
	A[0][0]=1;
    // first row all are '1' until obstacle
	for(int j=1;j<c;j++){
		if (A[0][j]==0){
			A[0][j]=A[0][j-1];
		}
		else{
			A[0][j]=0;
		}
	}
	// first column all are '1' until obstacle
	for(int i=1;i<r;i++){
		if(A[i][0]==0){
			A[i][0]=A[i-1][0];
		}
		else{
			// No ways to reach at this index
			A[i][0]=0;
		}
	}

	for(int i=1;i<r;i++){
		for(int j=1;j<c;j++){
			// If current cell has no obstacle
			if(A[i][j]==0){
				A[i][j]=A[i-1][j]+A[i][j-1];
			}
			else{
				// No ways to reach at this index
				A[i][j]=0;
			}
		}
	}
	return A[r-1][c-1];
}

int main()
{
    cin>>r; cin.ignore();
    cin>>c; cin.ignore();
    int A[10][10]={0};
    for(int i=0;i<r;i++) {
        string row;
        getline(cin,row);
        for(int j=0;j<c;j++){
            A[i][j]=row[j]-'0';
        }
    }

    cout<<numberOfPath(A)<<endl;
}
