import java.util.*;

class Solution {
    public long[] solution(int x, int n) {
        long[] answer = {};
        List<Long> list = new ArrayList<>();
        long temp = 0;
        for (int i=0; i<n; i++){
            temp += x;
            list.add(temp);
        }
        
        return list.stream().mapToLong(i -> i).toArray();
    }
}