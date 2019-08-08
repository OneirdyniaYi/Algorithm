#include <bits/stdc++.h>
using namespace std;

int dp[INT_MAX][INT_MAX];
void init(int n,int m){
	for(int i=0;i<=m;i++)
		dp[0][i] = 0;
	for(int i=0;i<=n;i++)
		dp[i][0] = 0;
} 
int LCS(string A,string B){
	int n = A.size();
	int m = B.size();
	init(n,m);
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(A[i] == B[j]){
				dp[i+1][j+1] = dp[i][j] + 1;	
			}else{
				dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j]);
			}
		}
	}
	return a[n][m];
}
string print(string A,string B){
	string res;
	int i = A.size();
	int j = B.size();
	while(dp[i][j]){
		if(dp[i][j]==dp[i-1][j]) i--;
		else if(dp[i][j]==dp[i][j-1]) j--;
		else{
			res = A[i-1] + res;		
			i--;j--;
		}
	}
	return res;
}

