// Greedy
#include<iostream>
#include<vector>
#include<algorithm>
#include<bits/stdc++.h>

using namespace std;

bool compare(const pair<int, int> &a, const pair<int, int> &b){
  if(a.second == b.second){
    return a.first > b.first;
  }
  return a.second < b.second;
}

int main(int argc, char** argv)
{
  int N = 0;
  cin >> N;
  int A = 0;
  int B = 0;

  vector<pair<int, int>> v;
  for(int i=0; i<N; i++){
    cin >> A >> B;
    pair<int, int> p(A, B);
    v.push_back(p);
  }
  
  sort(v.begin(), v.end(), compare);
  int prev_finish = v[0].second;
  int ans = 1;
  for(int it=1; it<v.size(); it++){
    // cout<<v[it].first<<' ' << v[it].second << '\n';
    if (v[it].first >= prev_finish){
      ans ++;
      prev_finish = v[it].second;
    }
  }

  cout << ans;
  
   return 0;
}