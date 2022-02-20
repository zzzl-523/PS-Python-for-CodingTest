import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        //로그 사용 자릿수 구하기 int zari = (int)(Math.log10(n)+1);
        
        String str = Integer.toString(n);
        for(int i=0; i<str.length(); i++){
            answer += Character.getNumericValue(str.charAt(i));
        }
        
        return answer;
    }
}