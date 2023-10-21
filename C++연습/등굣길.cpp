#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    
    // 위나 왼쪽에서만 올 수 있음
    vector<vector<int>> dp(m+1,vector<int>(n+1, 0));
    for(int i=0; i<puddles.size();i++){
        dp[puddles[i][0]][puddles[i][1]] = -1;
    }
    
    dp[1][1] = 1;
    for(int i=1;i<=m;i++){
        for (int j=1;j<=n;j++){
            if (dp[i][j]==-1){
                dp[i][j] = 0;
            }
            else{
                dp[i][j] += (dp[i-1][j] + dp[i][j-1])%1000000007;
            }  
        }
    }
    answer = dp[m][n];
    
    return answer;
}