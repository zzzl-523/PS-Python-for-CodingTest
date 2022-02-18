package java_practice;
public class 직사각형 {

    public static void main(String[] args){
        int[] ans = {};
        int[][] a = {{1, 4}, {3, 4}, {3, 10}};
        ans = solution(a);
        System.out.println(ans);
    }
    public static int[] solution(int[][] v) {
        int[] answer = {};
        int x_1 = v[0][0];
        int x_2 = 0;
        int y_1 = v[0][1];
        int y_2 = 0;

        for(int i=1; i<v.length; i++){
            if(v[i][0] == x_1){
                x_1 = -2;
            }else{
                x_2 = v[i][0];
            }
            if(v[i][0] == x_2){
                x_2 = -2;
            }

            if(v[i][1] == y_1){
                y_1 = -2;
            }else{
                y_2 = v[i][1];
            }
            if(v[i][1] == y_2){
                y_2 = -2;
            }
        }

        if(x_1 == -2){
            answer[0] = x_2;
        }else if(x_2 == -2){
            answer[0] = x_1;
        }

        if(y_1 == -2){
            answer[1] = y_2;
        }else if(y_2 == -2){
            answer[1] = y_1;
        }

        System.out.println(answer);
        return answer;
    }


}