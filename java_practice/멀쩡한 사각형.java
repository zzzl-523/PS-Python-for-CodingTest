import java.util.*;
class Solution {
    public long solution(long w, long h) {
        long answer = 0;
        for(int i=0; i<w; i++){
            answer += (i*h)/w;
        }
        
        return (long)answer*2;
    }
}