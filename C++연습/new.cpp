// 전체 돌면서 방문
// 방문했으면 값 바꾸기
// 크기는 개수

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
	vector<vector<char>> board(100);
	int N ;
	char input[100];
	cin >> N;
	

	for(int i=0;i<N;i++){
		vector<char> v;
		cin >> input;
		for(int j=0;j<N;j++){
			v.push_back(input[j]);
		}
		board[i] = v;
	}
	
	vector<pair<int,int>> d = {make_pair(0,1), make_pair(1,0), make_pair(0,-1), make_pair(-1,0)};
	
	int ans_cnt = 0;
	vector<int> ans; 
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			if(board[i][j]=='1'){
				queue<pair<int,int>> q;
				q.push(make_pair(i, j);
				
				int cnt = 0;
				ans_cnt ++;
				while(!q.empty()){
					pair<int, int> p = q.front();
					q.pop();
					int x,y;
					x = p.first;
					y = p.second;
					
					board[x][y] = 0;
					cnt ++;
					
					// cout<<d[0].first<<" "<<d[0].second<<endl;
					// cout<<"이거" << x<<y<<endl;
					for(int k=0;k<4;k++){
						int nx = x+d[k].first;
						int ny = y+d[k].second;
						
						
						
						if (nx<0||nx>N-1||ny<0||ny>N-1){
							continue;
						}
						
						if(board[nx][ny]=='1'){
							// cout<<nx<<ny<<endl;
							q.push(make_pair(nx, ny);
							board[nx][ny] = 0;
						}
						
						
					}
					
				}
				ans.push_back(cnt);
				// cout<<"숫자: "<<cnt;
				
			}
		}
	}
	cout << ans_cnt << endl;
	sort(ans.begin(), ans.end());
	for(int i=0;i<ans.size();i++){
		cout<<ans[i]<<" ";
	}
	
	return 0;
}