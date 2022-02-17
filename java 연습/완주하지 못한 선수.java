import java.util.Arrays;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        boolean is_in = false;
        
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        int j = 0;
        for(j=0; j<completion.length; j++){
            if(!participant[j].equals(completion[j])){
                break;
            }
        }
            
        return participant[j];
    }
}