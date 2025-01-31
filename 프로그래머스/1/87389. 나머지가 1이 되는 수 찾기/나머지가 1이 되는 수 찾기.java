       
// 나머지가 1이라는건, x * 몫 이 n-1 이라는 소린데. 그럼 x = n-1/몫. 몫은 1부터.
//     즉 x = n-1
// 근데 x가 다른 수로 나누어 떨어지면 그 나누는 수가 x가 된다. 재귀적인데.
// n이 홀수이면 답은 언제나 2야.
// n이 짝수이면.. n-1이 x인데 그보다 더 작은 x가 있느냐. 즉 n-1이 소수이냐 아니냐.
//     소수 판독을 해서 소수면 x값 그대로고, 소수 아니면 나눈다음에 다시 소수판독.
class Solution {
    public int solution(int n) {
        int answer = 0;
        if (n%2==1){
            return 2;
        }else{
            return getSosu(n-1);
        }
    }
    
    public int getSosu(int num){
        for(int i=2; i<num; i++){
            if(num % i == 0){
                return getSosu(i);
            }
        }
        return num;
        
    }

}