import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        Integer[] nums = new Integer[numbers.length];
        ArrayList<String> array = new ArrayList<String>();
        
        for(int i=0;i<numbers.length;i++){    
            array.add(Integer.toString(numbers[i]));
        }
     
        Collections.sort(array, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                return (b+a).compareTo(a+b);
                //오름차순 정렬 (o1+o2).compareTo(o1+o2);
            }
        });

        if(array.get(0).equals("0")){
            return "0";
        }
        for(String a : array){
            answer += a;
        }
        
        return answer;
    }
}