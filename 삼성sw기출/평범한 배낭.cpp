#include<bits/stdc++.h>
using namespace std;

//최대 무게 K , 물건의 개수 N, 무게 W, 가치 V
vector<pair<int, int>>bag;
int DP[105][100005];

int dp(int N, int K) {	//함수를 짤 때 조건을 생각해야 한다! (기저조건/메모이제이션)
	if (N == 0) {	//끝까지 확인하면 끝낸다(기저조건)
		return 0;
	}
	if (DP[N][K] != -1) {	//메모이제이션
		return DP[N][K];
	}

	DP[N][K] = 0;
	if (K >= bag[N].first) {
		return DP[N][K] = max(dp(N - 1, K), dp(N - 1, K - bag[N].first) + bag[N].second);
	}
	else {
		return DP[N][K] = dp(N - 1, K);
	}

}

int main() {
	memset(DP, -1, sizeof(DP)); //DP를 -1로 초기화
	int K, N;
	cin >> N >> K;
	
	bag.push_back({ 0,0 });	//0번째 값 리셋
	for (int i = 1; i <= N;i++) {
		int W, V;
		cin >> W >> V;
		bag.push_back({ W,V });
	}
	//top-down 방식
	cout << dp(N,K);
}