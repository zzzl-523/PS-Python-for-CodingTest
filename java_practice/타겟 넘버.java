class Solution {
    static int answer;
    
    public void dfs(int[] numbers, int target, int idx, int sum){
        if(idx == numbers.length){
            if(sum == target){
                answer++;
            }
            return;
        }

        sum += numbers[idx];
        dfs(numbers, target, idx+1, sum);
        sum -= (2*numbers[idx]);
        dfs(numbers, target, idx+1, sum);
    }
    
    public int solution(int[] numbers, int target) {
        answer = 0;
        dfs(numbers, target, 0, 0);
        return answer;
    }
}