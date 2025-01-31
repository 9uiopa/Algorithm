import java.util.*;

class Solution {
    public int[] solution(long n) {
        ArrayList<Integer> al = new ArrayList<>();
        while(n>0){
            int r = (int) (n % 10);
            n = n / 10;   
            al.add(r);
        }
        
        return al.stream().mapToInt(i->i).toArray();
    }
}