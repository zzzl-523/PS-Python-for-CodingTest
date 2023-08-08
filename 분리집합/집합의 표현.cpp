#include<iostream>
#include<string>
using namespace std;

int parent[1000005];

int find(int node) {
	if (parent[node] == node) {
		return node;
	}
	return parent[node] = find(parent[node]);
}
void _union(int a, int b) {
	a = find(a);
	b = find(b);
	if (a != b) {
		parent[a] = b;
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int n, m;
	cin >> n >> m;
	
	for (int i = 0; i <= n; i++) {
		parent[i] = i;
	}

	while (m--) {
		int menu, a, b;
		cin >> menu >> a >> b;

		if (menu == 0) {
			_union(a, b);
		}
		else if (menu == 1) {
			if (find(a) == find(b)) {
				cout << "YES\n";
			}
			else {
				cout << "NO\n";
			}
		}
	}
	return 0;
}