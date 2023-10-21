#include<vector>
#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;

void bfs();
vector<vector<int>> board = {{}};
vector<vector<int>> visited = {{}};
vector<vector<int>> d = {{-1,0}, {0,1}, {1,0}, {0,-1}};
int INF = 123456789;

int solution(vector<vector<int> > maps)
{
    int answer = 0;
    board = maps;
    visited = maps;
    for(int i=0; i<maps.size(); i++) {
        for(int j=0; j<maps[0].size(); j++) {
            board[i][j] = INF;
            visited[i][j] = 0;
        }
    }

    
    // bfs
    queue<pair<int, int>> q;
    q.push({0, 0});
    board[0][0] = maps[0][0];

    
    while (!q.empty()) {
        pair<int, int> now = q.front();
        q.pop();
        int x = now.first;
        int y = now.second;
        
        if (not visited[x][y]) {
            visited[x][y] = 1;
        
            for(int i=0; i<d.size(); i++){
                int nx = x + d[i][0];
                int ny = y + d[i][1];

                if (nx<0 || nx>maps.size()-1 || ny<0 || ny>maps[0].size()-1 || maps[nx][ny]==0){
                    continue;
                }

                board[nx][ny] = min(board[nx][ny], board[x][y]+maps[nx][ny]);
                q.push({nx, ny});
            }
        }
    }
    
    answer = board[maps.size()-1][maps[0].size()-1];
    if (answer == INF) {
        return -1;
    }
    
    return answer;
}

