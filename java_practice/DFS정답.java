import java.util.ArrayList;

public class solution{
    public static void main(String [] args){
        int[][] train = {{1,2},{1,3},{1,4},{3,5}, {3,6}};
        int[] passenger = {1,1,1,1,1,1};
        int n = 6;

        solution(n, passenger, train);
    }

    public static int[] solution(int n, int[] passenger, int[][] train) {
        int[] visited = new int[n + 1];
        sss = new int[n+1];
        sss[1] = passenger[0];
        ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
        for(int i=0; i<n+1; i++){
            graph.add(new ArrayList<Integer>());
        }
        for(int i=0; i<train.length; i++){
            graph.get(train[i][0]).add(train[i][1]);
            graph.get(train[i][1]).add(train[i][0]);
        }

        dfs(graph, passenger, visited, 1, 0);
        int max = 0;
        int max_idx = 0;
        for(int i=1; i<sss.length; i++){
            if(max <= sss[i]){
                max = sss[i];
                max_idx = i;
            }
        }
        int[] answer = {max_idx, max};
        return answer;
    }

    public static int[] sss = {};
    public static void dfs(ArrayList<ArrayList<Integer>> graph, int[] nums, int[] visited, int v, int sum){
        visited[v] = 1;
        sum += nums[v-1];
        sss[v] = sum;

        for(int i : graph.get(v)){
            if(visited[i] == 0) {
                dfs(graph, nums, visited, i, sum);
            }
        }

    }
}