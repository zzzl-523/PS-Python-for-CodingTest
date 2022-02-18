class Solution
{
    public int solution(int [][]board)
    {
        int answer = 0;
        int sero = board.length;
        int garo = board[0].length;
        int[][] DP = new int[sero][garo];
        int max = 0;

        DP[0] = board[0];
        for(int i=0; i<garo; i++){
            if(DP[0][i]==1){
                max = 1;
                break;
            }
        }

        for(int i=1; i<sero; i++){
            for(int j=0; j<garo; j++){
                DP[i][j] = board[i][j];
                if(DP[i][j] == 1 && (j>0)){
                    int left = DP[i][j-1];
                    int up = DP[i-1][j];
                    int upleft = DP[i-1][j-1];
                    
                    DP[i][j] = Math.min(left, Math.min(up, upleft)) + 1;
                    max = Math.max(max, DP[i][j]);
                }
            }
        }
        answer = max*max;
        return answer;
    }
}