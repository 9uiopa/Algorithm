
class Solution {
    public long solution(int a, int b) {
        if (a==b) return a;
        int big = Math.max(a,b);
        int small = Math.min(a,b);
        long answer=0;
        
        for(int i = small; i<=big; i++){
            answer+= i;
        }
        return answer;
    }
}