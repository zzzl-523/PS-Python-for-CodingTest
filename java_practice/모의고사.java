import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> ans = new ArrayList<Integer>();
        
        int[] cnt = {0, 0, 0};
        int[] student_1 = {1, 2, 3, 4, 5};
        int[] student_2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] student_3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        for(int i=0; i<answers.length; i++){
            if(answers[i] == student_1[i%student_1.length]){
                cnt[0]++;
            }
            if(answers[i] == student_2[i%student_2.length]){
                cnt[1]++;
            }
            if(answers[i] == student_3[i%student_3.length]){
                cnt[2]++;
            }
        }
        
        int max = 0;
        int max_index = -1;
        for(int i=0; i<cnt.length; i++){
            if(max < cnt[i]){
                max = cnt[i];
                max_index = i;
            }
        }
        
        for(int i=0; i<cnt.length; i++){
            if(cnt[i] == max){
                ans.add(i+1);
            }
        }
        Collections.sort(ans);
        
        int[] answer = new int[ans.size()];
        int size = 0;
        for(int temp : ans){
            answer[size++] = temp;
        }
        
        
        return answer;
    }
}