#include <string>
#include <vector>
#include <iostream>

using namespace std;

// - 곱한 것과 아닌 것으로 dfs
void dfs(int idx, int total);
int answer = 0;
vector<int> arr = {0};
int goal = 0;

int solution(vector<int> numbers, int target) {
    arr = numbers;
    goal = target;
    
    dfs(0, 0);

    return answer;
}

void dfs(int idx, int total){
    if (idx > arr.size()-1) {
        if (total == goal) {
            answer += 1;
        }
        return;
    }
    
    // 그대로
    dfs(idx+1, total + arr[idx]);
    
    // -로 만들기
    dfs(idx+1, total + (-1)*arr[idx]);
}