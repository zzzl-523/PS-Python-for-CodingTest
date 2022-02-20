class Solution {
    public int[] solution(int[][] v) {
        int[] answer = {0, 0};
        int x_1 = v[0][0];
        int x_2 = 0;
        int y_1 = v[0][1];
        int y_2 = 0;
        int cnt_x = 0;
        int cnt_y = 0;

        for(int i=1; i<v.length; i++){
            if(v[i][0] == x_1){
                cnt_x = 2;
            }else{
                x_2 = v[i][0];
            }


            if(v[i][1] == y_1){
                cnt_y = 2;
            }else{
                y_2 = v[i][1];
            }
        }

        if(cnt_x == 2){
            answer[0] = x_2;
        }else{
            answer[0] = x_1;
        }

        if(cnt_y == 2){
            answer[1] = y_2;
        }else{
            answer[1] = y_1;
        }

        return answer;
    }
}