
class Solution {
    public boolean solution(int x) {
        int num = x;
        int sum = 0;
        while(x>0){
            int r = x % 10;
            sum += r;
            x = x / 10;
        }
        if (num % sum == 0){
            return true;
        }else{
            return false;
        }

    }
}