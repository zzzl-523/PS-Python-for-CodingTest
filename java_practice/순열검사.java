import java.util.*;

class Solution {
    public boolean solution(int[] arr) {
        boolean answer = true;
        int[] counter = new int[arr.length];
        
        Arrays.sort(arr);
        for(int i=0; i<arr.length; i++){
            if(arr[i] == i+1){
                counter[i]++;    
                if(i == arr.length-1){
                    return answer;
                }
            }else{
                answer = false;
                return answer;
            }
        }
        System.out.println("Hello Java");

        return answer;
    }
}